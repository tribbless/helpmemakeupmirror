import cv2
import numpy as np
from personalColor.personal_color_analysis import tone_analysis
from personalColor.personal_color_analysis.detect_face import DetectFace
from personalColor.personal_color_analysis.color_extract import DominantColors
from colormath.color_objects import LabColor, sRGBColor, HSVColor
from colormath.color_conversions import convert_color

def analysis(imgpath):
    #######################################
    #           Face detection            #
    #######################################
    df = DetectFace(imgpath) #
    #print("df : ",df)

    face = [df.left_cheek, df.right_cheek,
            df.left_eyebrow, df.right_eyebrow,
            df.left_eye, df.right_eye]

    if(len(face[0]) == 0):
        return False
    else:
        #######################################
        #         Get Dominant Colors         #
        #######################################
        temp = []
        clusters = 4
        for f in face:
            dc = DominantColors(f, clusters)
            face_part_color, _ = dc.getHistogram()
            #dc.plotHistogram()
            temp.append(np.array(face_part_color[0]))
        cheek = np.mean([temp[0], temp[1]], axis=0)
        eyebrow = np.mean([temp[2], temp[3]], axis=0)
        eye = np.mean([temp[4], temp[5]], axis=0)

        Lab_b, hsv_s = [], []
        color = [cheek, eyebrow, eye]
        for i in range(3):
            rgb = sRGBColor(color[i][0], color[i][1], color[i][2], is_upscaled=True)
            lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
            hsv = convert_color(rgb, HSVColor, through_rgb_type=sRGBColor)
            Lab_b.append(float(format(lab.lab_b,".2f")))
            hsv_s.append(float(format(hsv.hsv_s,".2f"))*100)

        print('Lab_b[skin, eyebrow, eye]',Lab_b)
        print('hsv_s[skin, eyebrow, eye]',hsv_s)
        #######################################
        #      Personal color Analysis        #
        #######################################
        Lab_weight = [30, 20, 5]
        hsv_weight = [10, 1, 1]
        if(tone_analysis.is_warm(Lab_b, Lab_weight)):
            if(tone_analysis.is_spr(hsv_s, hsv_weight)):
                tone = 'SPRING WARM'
            else:
                tone = 'FALL WARM'
        else:
            if(tone_analysis.is_smr(hsv_s, hsv_weight)):
                tone = 'SUMMER COOL'
            else:
                tone = 'WINTER COOL'
        # Print Result
        print('{}의 퍼스널 컬러는 {}입니다.'.format(imgpath, tone))
        return tone
