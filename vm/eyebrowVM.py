import cv2
import dlib
import imutils
from pylab import *
import numpy as np

class Eyebrow:
    def __init__(self, kind, color, makeupFace):
        self.kind = kind
        self.color = color
        self.makeupFace = makeupFace
        #self.color = color

    def eyebrow_Apply(self, landmark):
        # landmark 저장
        pts1 = np.array(landmark[17:22], np.int32)  # 왼쪽 눈썹 위치 landmark 값을 pts1에 저장 : 점 18~22
        pts2 = np.array(landmark[22:27], np.int32)  # 오른쪽 눈썹 위치 landmark 값을 pts2에 저장 : 점 23~27

        # eyebrow_kind_image select
        print(self.kind)
        if self.kind == "straight":
            if color == "black":
                left_eye = cv2.imread('eyebrow/straight/straight_black_left_eyebrow.png', -1)
                right_eye = cv2.imread('eyebrow/straight/straight_black_right_eyebrow.png', -1)
            elif color == "brown":
                left_eye = cv2.imread('eyebrow/straight/straight_brown_left_eyebrow.png', -1)
                right_eye = cv2.imread('eyebrow/straight/straight_brown_right_eyebrow.png', -1)

        elif self.kind =="arch":
            if color == "black":
                left_eye = cv2.imread('eyebrow/arch/arch_black_left_eyebrow.png', -1)
                right_eye = cv2.imread('eyebrow/arch/arch_black_right_eyebrow.png', -1)
            elif color == "brown":
                left_eye = cv2.imread('eyebrow/arch/arch_brown_left_eyebrow.png', -1)
                right_eye = cv2.imread('eyebrow/arch/arch_brown_right_eyebrow.png', -1)

        '''left eyebrow'''

        # rescale : 눈썹이미지의 width를 'landmark 22의 x값 - 18의 x값' 길이에 맞춰 눈썹이미지 크기 조절
        scale = float(pts1[4][0] - pts1[0][0]) / left_eye.shape[1] # right_eye.shape[1] : 눈썹이미지 width
        left_eye = cv2.resize(left_eye, (0, 0), fx=scale, fy=scale)

        # find location
        x_offset = pts1[0][0]  # landmark 18(눈썹부분에 첫번째 점)에 x값
        y_offset = pts1[0][1]  # landmark 18에 y값
        y2 = y_offset  # landmark 18에 y값
        y1 = y_offset - left_eye.shape[0]  # landmark 18에 y값 - 눈썹이미지 height


        ## x값은 오른쪽으로 갈수록 커지고, y값은 위로 갈수록 커집니다 !!!!!

        # interval값 찾기 (li = left interval)
        #  >> 왼쪽 눈썹에 해당하는 landmark 18~22 y값의 최소값 찾기 (가장 위쪽에 있는 값 찾기)
        #  >> left_i(y값의 최솟값과 y1값 차이)를 y1,y2에 각각 더해

        min_y = pts1[0][1]
        for i in range(1, 5):
            if (min_y > pts1[i][1]):
                min_y = pts1[i][1]
        left_i = abs(min_y - y1) # left_i : y값의 최솟값과 y1값 차이

        y2 = y_offset + left_i
        y1 = y_offset - left_eye.shape[0] + left_i

        x1 = x_offset  # x값
        x2 = x_offset + left_eye.shape[1]  # x값 + 눈썹 이미지 너비(landmark 22-18 값)



        ### '눈썹이미지 - face'를 Blending

        # normalize alpha channels from 0-255 to 0-1(0:투명도 100% , 1:투명도 0%)
        alpha_s = left_eye[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s # 투명도 100%

        # set adjusted colors
        for c in range(0, 3):
            makeupFace[y1:y2, x1:x2, c] = (alpha_s * left_eye[:, :, c] + alpha_l * makeupFace[y1:y2, x1:x2, c])

        #for c in range(0, 3):
        #    face[y1:y2, x1:x2, c] = (alpha_s * left_eye[:, :, c] + alpha_l * face[y1:y2, x1:x2, c])
            #print(c,face)
            #print(c,left_eye[:, :, c])
            #print(c,alpha_s * left_eye[:, :, c])
            #print(c,alpha_l * face[y1:y2, x1:x2, c])

        '''right eyebrow'''

        # rescale
        scale = float(pts2[4][0] - pts2[0][0]) / right_eye.shape[1]
        right_eye = cv2.resize(right_eye, (0, 0), fx=scale, fy=scale)

        # find location
        x_offset = pts2[0][0]  # landmark 23 x좌표
        y_offset = pts2[0][1]  # landmark 23 y좌표
        y1 = y_offset - right_eye.shape[0]
        y2 = y_offset

        ## x값은 오른쪽으로 갈수록 커지고, y값은 위로 갈수록 커집니다 !!!!!

        # interval값 찾기 (ri = right interval)
        #  >> 왼쪽 눈썹에 해당하는 landmark 18~22 y값의 최소값 찾기 (가장 위쪽에 있는 값 찾기)
        #  >>
        min_y = pts2[0][1]
        for i in range(1, 5):
            if (min_y > pts2[i][1]):
                min_y = pts2[i][1]
        right_i = abs(min_y - y1)

        y1 = y_offset - right_eye.shape[0] + right_i
        y2 = y_offset + right_i

        x1 = x_offset
        x2 = x_offset + right_eye.shape[1]



        alpha_s = right_eye[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        #print(alpha_l)
        #print(alpha_s)

        # apply eyebrow
        for c in range(0, 3):
            makeupFace[y1:y2, x1:x2, c] = (alpha_s * right_eye[:, :, c] + alpha_l * makeupFace[y1:y2, x1:x2, c])

        #for c in range(0, 3):
        #    face[y1:y2, x1:x2, c] = (alpha_s * right_eye[:, :, c] + alpha_l * face[y1:y2, x1:x2, c])
        return makeupFace


def makeupFace_face_blending(face, makeupFace, alpha):
    ### makeupFace와 face Blending - alpha값에 따라 눈썹 투명도 조절 가능
    cv2.addWeighted(makeupFace, alpha, face, 1 - alpha, 0, face)
    return face


## image read
face = cv2.imread('test_image/ex2.jpg')  # -1 : 이미지 파일을 3alpha channel 까지 포함해 읽음
makeupFace = face.copy()

color = "black"
#color = "brown"

## landmark

# dlib에 있는 정면 얼굴검출기로 입력 사진에서 얼굴 검출하여 detected_faces로 변환
detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor("../face_detector/shape_predictor_68_face_landmarks.dat")

detected_faces = detector(face, 0) # detected_faces : rectangles[[(66, 137) (281, 352)]]
pose_landmarks = face_pose_predictor(face, detected_faces[0]) # detected_face[0] : rectangle(66,137,281,352)

landmark = np.empty([68, 2], dtype=int)
for i in range(68):
    landmark[i][0] = pose_landmarks.part(i).x #x값(가로)
    landmark[i][1] = pose_landmarks.part(i).y #y값(세로)

#StraightEyebrow = Eyebrow("straight", color, makeupFace)
#makeupFace = StraightEyebrow.eyebrow_Apply(landmark)
ArchEyebrow = Eyebrow("arch", color, makeupFace)
makeupFace = ArchEyebrow.eyebrow_Apply(landmark)

#투명도 조절할 때
alpha = 1.0
face = makeupFace_face_blending(face, makeupFace, alpha)

face = imutils.resize(face, width=600)

#cv2.imwrite("./result3/brown7.png",face)
cv2.imshow('after', face)
cv2.waitKey(0)
cv2.destroyAllWindows()