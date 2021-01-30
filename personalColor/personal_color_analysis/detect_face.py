# coding: utf-8
# import the necessary packages
from imutils import face_utils
import numpy as np
import dlib
import cv2

class DetectFace:
    #2
    def __init__(self, image):
        # initialize dlib's face detector (HOG-based)
        # and then create the facial landmark predictor
        self.detector = dlib.get_frontal_face_detector() # dlib.fhog_object_detector 객체 생성,, ,얼굴 검출에 사용
        self.predictor = dlib.shape_predictor('face_detector/shape_predictor_68_face_landmarks.dat') # 얼굴 랜드 마크 탐지
        #self.predictor = dlib.shape_predictor('../face_detector/shape_predictor_68_face_landmarks.dat') # 얼굴 랜드 마크 탐지

        #face detection part
        self.img = cv2.imread(image)
        #if self.img.shape[0]>500:
        #    self.img = cv2.resize(self.img, dsize=(0,0), fx=0.8, fy=0.8)
        # face detection part
        #self.img = cv2.imread(image)

        # init face parts
        self.right_eyebrow = []
        self.left_eyebrow = []
        self.right_eye = []
        self.left_eye = []
        self.left_cheek = []
        self.right_cheek = []

        # detect the face parts and set the variables
        self.detect_face_part() #


    # return type : np.array
    def detect_face_part(self):
        #face_parts = [[],[],[],[],[],[],[]]
        face_parts = [[],[],[],[],[],[],[],[]]
        # detect faces in the grayscale ## image 얼굴 검출
        face_cascade = cv2.CascadeClassifier("face_detector/haarcascade_frontalface_default.xml")
        # 색상 변환 cvtColor BGR > RGB
        image= cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        #print(image)
        # 색상 변환 cvtColor RGB > GRAY (회색)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # detectMultiScale : input 이미지에서 크기가 다른 object 검출하는 함수
        # gray : 검출하고자 하는 원본 이미지. 1.3 : 검색 윈도우 확대 비율, 5 : 검출 영역으로 선택하기 위한 최소 검출 횟수
        # 근데 따로 지정 없어서 정확하지 X, 원래 인자는 7개 정도 됨
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        result = True
        if len(faces) != 1:
            result = False
            print("얼굴인식 실패")
            shape = 0
            return result
        else:
            rect = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)[0]


            # determine the facial landmarks for the face region, then
            # convert the landmark (x, y)-coordinates to a NumPy array
            shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
            # 얼굴 검출과 랜드마크 검출 정도 느낌인거같고

            # 얼굴 부위의 얼굴 랜드마크를 결정하고, 그 다음
            # 얼굴 랜드마크(x, y) 좌표를 NumPy로 변환
            # 배열
            shape = face_utils.shape_to_np(shape)

            idx = 0
            # loop over the face parts individually
        #     print("face_utils.FACIAL_LANDMARKS_IDXS.items() :", face_utils.FACIAL_LANDMARKS_IDXS.items(), "num : ", len(face_utils.FACIAL_LANDMARKS_IDXS.items()))
            print("")
            # 얼굴 부분을 개별적으로 루프,,, 얼굴을 군데군데 분류 왼쪽 눈썹, 오른쪽 눈썹, 왼쪽 눈, 오른쪽 눈, 왼쪽 피부, 오른쪽 피부
            for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                face_parts[idx] = shape[i:j] #
                idx += 1
            #face_parts = face_parts[1:5]
            face_parts = face_parts[2:6]
                # set the variables
                # Caution: this coordinates fits on the RESIZED image.
            self.right_eyebrow = self.extract_face_part(face_parts[0])
            self.left_eyebrow = self.extract_face_part(face_parts[1])
            self.right_eye = self.extract_face_part(face_parts[2])
            self.left_eye = self.extract_face_part(face_parts[3])
                # Cheeks are detected by relative position to the face landmarks
            self.left_cheek = self.img[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]]
            self.right_cheek = self.img[shape[29][1]:shape[33][1], shape[54][0]:shape[12][0]]


    # parameter example : self.right_eye
    # return type : image
    def extract_face_part(self, face_part_points): # 추가 분석 필요
        # boundingRect : 윤곽선의 경계면을 둘러싸는 사각형 계산
        (x, y, w, h) = cv2.boundingRect(face_part_points)
        # x, w 가 너비같고 y, h가 높이같음
        crop = self.img[y:y+h, x:x+w]
        adj_points = np.array([np.array([p[0]-x, p[1]-y]) for p in face_part_points])

        # Create an mask
        mask = np.zeros((crop.shape[0], crop.shape[1]))
        cv2.fillConvexPoly(mask, adj_points, 1)
        mask = mask.astype(np.bool)
        crop[np.logical_not(mask)] = [255, 0, 0]

        return crop