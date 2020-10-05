import cv2
import dlib
from pylab import *
import numpy as np
from scipy.interpolate import interp1d

class Eyeliner:
    def __init__(self, kind, color, makeupFace):
        self.kind = kind
        self.makeupFace = makeupFace # 얼굴사진 복사본
        self.color = color

    def get_upper_eyelids(self, landmarks, flag=None):
        """
        Find out landmarks corresponding to upper eyes.
        """
        if landmarks is None:
            return None
        liner = ""
        for point in landmarks[36:40]:  # left eye 위쪽
            liner += str(point).replace('[', '').replace(']', '') + '\n'  # [] => 없애기
        liner += '\n'
        for point in landmarks[42:46]:  # right eye 위쪽
            liner += str(point).replace('[', '').replace(']', '') + '\n'  # [] => 없애기
        return liner

    def draw_liner(self, eye, direction):
        """
        Draws eyeliner.
        """
        eye_x = []
        eye_y = []
        x_points = []
        y_points = []
        newP_X = []
        newP_Y =[]
        for point in eye:
            x_points.append(int(point.split()[0]))  # x_points = [257, 268, 284, 299] # points.split() => 스페이스바로 나누기
            y_points.append(int(point.split()[1]))

        ## 왼쪽 눈 적용
        if direction == 'left':
            ## eyeliner 방향 조절
            newP_X = x_points[0] - abs((x_points[0] - x_points[3]) / 4)
            if self.kind == "Middle":
                newP_Y = y_points[0]
            elif self.kind == "Up":
                newP_Y = y_points[1] + abs(y_points[1] - y_points[0]) * 2 / 3
            elif self.kind == "Down":
                newP_Y = y_points[0] + abs(y_points[1] - y_points[0]) * 1 / 3
            ## 새로운 점 x_points, y_points 추가하기
            x_points.insert(0,int(newP_X))
            y_points.insert(0,int(newP_Y))

            curve = interp1d(x_points, y_points, 'quadratic', bounds_error=False)
            for point in np.arange(x_points[len(x_points) - 1], x_points[0], -1):
                eye_x.append(point)
                eye_y.append(int(curve(point)))

            ## 새로운 점과 오리지널 점[1]과 잇기
            x_Npoints = [x_points[0], x_points[2],x_points[3],x_points[4]]
            y_Npoints = [y_points[0], y_points[2],y_points[3]-1,y_points[4]]
            curve = interp1d(x_Npoints, y_Npoints, 'linear')
            for point in np.arange(x_Npoints[0], x_Npoints[len(x_Npoints) - 1] + 1, 1):
                eye_x.append(point)
                eye_y.append(int(curve(point)))



        ## 오른쪽 눈 적용
        elif direction == 'right':
            ## eyeliner 방향 조절
            newP_X = x_points[3] + abs((x_points[0] - x_points[3]) / 4)
            if self.kind == "Middle":
                newP_Y = y_points[3]
            elif self.kind == "Up":
                newP_Y = y_points[2] + abs(y_points[2] - y_points[3]) * 2 / 3
            elif self.kind == "Down":
                newP_Y = y_points[3] + abs(y_points[2] - y_points[3]) * 1 / 3

            ## 새로운 점 x_points, y_points 추가하기
            x_points.append(int(newP_X))
            y_points.append(int(newP_Y))

            curve = interp1d(x_points, y_points, 'quadratic', bounds_error=False)
            for point in np.arange(x_points[1], x_points[len(x_points) - 1], 1):
                eye_x.append(point)
                eye_y.append(int(curve(point)))

            ## 새로운 점과 오리지널 점[2]과 잇기
            x_Npoints = [x_points[0],x_points[1],x_points[2],x_points[4]]
            y_Npoints = [y_points[0],y_points[1]-1,y_points[2], y_points[4]]
            curve = interp1d(x_Npoints, y_Npoints, 'linear')
            for point in np.arange(x_Npoints[len(x_Npoints) - 1], x_Npoints[0], -1):
                eye_x.append(point)
                eye_y.append(int(curve(point)))

        curve = zip(eye_x, eye_y)  ## list(zip([1, 2, 3], [4, 5, 6]))    =>      [(1, 4), (2, 5), (3, 6)]
        #plt.plot(eye_x, eye_y, color='green', linewidth=1)
        points = []
        for point in curve:
            points.append(np.array(point, dtype=np.int32))
        points = np.array(points, dtype=np.int32)
        #cv2.fillPoly(makeupFace, [points], 1)## fillPoly : 도형안을 색칠해주는 함수
        cv2.fillPoly(makeupFace, [points], color)
        return makeupFace


    def create_eye_liner(self,eyes_points):
        """
        Apply eyeliner.
        """
        left_eye = eyes_points[0].split('\n')  # \n 중심으로 나누기
        right_eye = eyes_points[1].split('\n')
        right_eye = right_eye[0:4]
        self.draw_liner(left_eye, 'left')  ## left eye : eyeliner 적용
        self.draw_liner(right_eye, 'right')  ## right eye : eyeliner 적용
        #self.makeupFace_face_blending()
        return

    def eyeliner_Apply(self,landmarks):
        liner = self.get_upper_eyelids(landmarks)
        eyes_points = liner.split('\n\n')
        self.create_eye_liner(eyes_points)
        return makeupFace

def makeupFace_face_blending(face, makeupFace, alpha):
    ### makeupFace와 face Blending - alpha값에 따라 투명도 조절 가능
    cv2.addWeighted(makeupFace, alpha, face, 1 - alpha, 0, face)
    return face

## image read
face = cv2.imread('./test_image/ex4.jpg') #-1 : 이미지 파일을 3alpha channel 까지 포함해 읽음  *original*
makeupFace = face.copy() ## 얼굴이미지 복사본 for 아이라이너와 오버레이 *makeup*
#black
black = (0, 0, 0)
#brown1
brown1 = (36, 46, 83)
#brown2
brown2 = (34, 42, 70)
color = black

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


#처음 모양과 색깔 주어졌을 때
midEyeliner = Eyeliner("Middle", color, makeupFace)
makeupFace = midEyeliner.eyeliner_Apply(landmark)
#upEyeliner = Eyeliner("Up", color, makeupFace)
#makeupFace = upEyeliner.eyeliner_Apply(landmark)

#투명도 조절할 때
alpha = 1.0
face = makeupFace_face_blending(face, makeupFace, alpha)



##downEyeliner = Eyeliner("Down",face,copy)
##face = downEyeliner.eyeliner_Apply(landmark)


#for n in range(42, 46):
#    cv2.circle(face, (landmark[n][0], landmark[n][1]), 1, (255, 0, 0), -1)

# 출력
#face = imutils.resize(face, width=800)
#face = imutils.resize(face, height=600) # 1,5,6 가로가 기네

#cv2.imwrite("./result4/v3_4.jpg",face)
cv2.imshow('after', face)
cv2.waitKey(0)
cv2.destroyAllWindows()