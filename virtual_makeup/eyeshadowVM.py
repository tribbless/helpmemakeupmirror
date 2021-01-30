from scipy.interpolate import interp1d, pchip
from pylab import *
from skimage import color
import cv2

class eyeshadow_class(object):
    def __init__(self, R, G, B, type, img, coordinate_value):
        self.R = R
        self.G = G
        self.B = B
        self.type = type
        self.lower_left_end = 5
        self.upper_left_end = 11
        self.lower_right_end = 16
        self.upper_right_end = 22
        self.L_shadow, self.A_shadow, self.bB_shadow = 0, 0, 0
        self.x = []
        self.y = []
        self.xleft = []
        self.yleft = []
        self.xright = []
        self.yright = []
        self.file_shadow = np.loadtxt(coordinate_value)
        self.img = img

#    def inter_shadow(self, lx=[], ly=[], k1='quadratic'): 너무 휙휙 바뀜 보간법 어려워 nearest
    def inter_shadow(self, lx=[], ly=[], k1='quadratic'):
        unew = np.arange(lx[0], lx[-1] + 1, 1)
        ln_x = len(unew)
        newx = np.linspace(lx.min(),lx.max(), ln_x)
        f3 = pchip(lx, ly)(newx)
        f3 = interp1d(newx, f3, kind=k1, bounds_error=False)
        f2 = interp1d(lx, ly, kind=k1, bounds_error=False)
        return (f3, unew)

    def ext_shadow(self, a, b, i):  # 여기서 float 형이 된다.

        self.x.extend(arange(a, b, 1, dtype=np.int32).tolist())  # list 값 추가 dtype = np.int32를 이용해서 [:] 이런 슬라이스 오류 해결

        if (b - a == 1):
            self.y.extend((ones(int(b - a), dtype=np.int32) * i).tolist())
        else:
            self.y.extend((ones(int(b - a + 1), dtype=np.int32) * i).tolist())

    def extleft_shadow(self, a, b, i):
        self.xleft.extend(arange(a, b, 1).tolist())  # xleft list 값 추가
        if (b - a == 1):
            self.yleft.extend((ones(int(b - a), dtype=np.int32) * i).tolist())
        else:
            self.yleft.extend((ones(int(b - a + 1), dtype=np.int32) * i).tolist())

    def extright_shadow(self, a, b, i):
        self.xright.extend(arange(a, b, 1).tolist())
        if (b - a == 1):
            self.yright.extend((ones(int(b - a), dtype=np.int32) * i).tolist())
        else:
            self.yright.extend((ones(int(b - a + 1), dtype=np.int32) * i).tolist())

    def small_shadow(self, point_y, point_y_down, point_y_right, point_y_right_down, offset_left, offset_right):
        point_y[0] += offset_left * 0.725  # 그대로
        point_y[1] += offset_left * 0.51  # +0.1 원래 0.3
        point_y[2] += offset_left * 0.46  # +0.11 원래 0.15
        point_y[3] += offset_left * 0.41  # +0.1 원래 0.1 ->  0.51
        point_y[4] += offset_left * 0.51  # +0.1 원래 0.2
        point_y_down[0] += offset_left * 0.725  # 그대로

        point_y_right[-1] += offset_right * 0.725  # 그대로 (0.625)
        point_y_right[1] += offset_right * 0.51  # +0.1 원래 0.2
        point_y_right[2] += offset_right * 0.41  # +0.1 원래 0.1
        point_y_right[3] += offset_right * 0.451  # # +0.1해서 원래 0.25인데 오류 발생해서 0.251로 함 완전 원래 0.15
        point_y_right[4] += offset_right * 0.51  # +0.1 원래 0.3
        point_y_right_down[-1] += offset_right * 0.725  # 그대로

    def middle_shadow(self, point_y, point_y_down, point_y_right, point_y_right_down, offset_left, offset_right):
        point_y[0] += offset_left * 0.625  # 그대로
        point_y[1] += offset_left * 0.51  # +0.1 원래 0.3
        point_y[2] += offset_left * 0.36  # +0.11 원래 0.15
        point_y[3] += offset_left * 0.31  # +0.1 원래 0.1 ->  0.51
        point_y[4] += offset_left * 0.41  # +0.1 원래 0.2
        point_y_down[0] += offset_left * 0.625  # 그대로

        point_y_right[-1] += offset_right * 0.625  # 그대로 (0.625)
        point_y_right[1] += offset_right * 0.41  # +0.1 원래 0.2
        point_y_right[2] += offset_right * 0.31  # +0.1 원래 0.1
        point_y_right[3] += offset_right * 0.351  # # +0.1해서 원래 0.25인데 오류 발생해서 0.251로 함 완전 원래 0.15
        point_y_right[4] += offset_right * 0.51  # +0.1 원래 0.3
        point_y_right_down[-1] += offset_right * 0.625  # 그대로


    def large_shadow(self, point_y, point_y_down, point_y_right, point_y_right_down, offset_left, offset_right):
        point_y[0] += offset_left * 0.525  # 그대로
        point_y[1] += offset_left * 0.31  # +0.1 원래 0.3
        point_y[2] += offset_left * 0.26  # +0.11 원래 0.15
        point_y[3] += offset_left * 0.21  # +0.1 원래 0.1 ->  0.51
        point_y[4] += offset_left * 0.31  # +0.1 원래 0.2
        point_y_down[0] += offset_left * 0.525  # 그대로

        point_y_right[-1] += offset_right * 0.525  # 그대로 (0.625)
        point_y_right[1] += offset_right * 0.31  # +0.1 원래 0.2
        point_y_right[2] += offset_right * 0.21  # +0.1 원래 0.1
        point_y_right[3] += offset_right * 0.251  # # +0.1해서 원래 0.25인데 오류 발생해서 0.251로 함 완전 원래 0.15
        point_y_right[4] += offset_right * 0.41  # +0.1 원래 0.3
        point_y_right_down[-1] += offset_right * 0.525  # 그대로

    def eyeshadow_makeup(self):
        points = np.floor(self.file_shadow)
        point_down_x = np.array((points[:self.lower_left_end][:, 0]))
        point_down_y = np.array(points[:self.lower_left_end][:, 1])
        point_up_x = np.array(points[self.lower_left_end:self.upper_left_end][:, 0])
        point_up_y = np.array(points[self.lower_left_end:self.upper_left_end][:, 1])
        point_down_x_right = np.array((points[self.upper_left_end:self.lower_right_end][:, 0]))
        point_down_y_right = np.array(points[self.upper_left_end:self.lower_right_end][:, 1])
        point_up_x_right = np.array((points[self.lower_right_end:self.upper_right_end][:, 0]))
        point_up_y_right = np.array(points[self.lower_right_end:self.upper_right_end][:, 1])

        # imread,,, 그래픽 파일에서 이미지 읽어오는 코드
        #im = imread(self.img)
        im = self.img
        point_down_y_max = max(point_down_y)  # 최대값 지정 (왼쪽이라 추정)
        point_up_y_min = min(point_up_y)  # 최소값 지정
        offset_left = point_down_y_max - point_up_y_min  # 왼쪽 위치 지정

        point_down_y_right_max = max(point_down_y_right)  # 오른쪽 최대값 지정
        point_up_y_right_min = min(point_up_y_right)  # 오른쪽 최소값 지정 ( 포인트 최소값 )
        offset_right = point_down_y_right_max - point_up_y_right_min  # 오른쪽 위치 지정

        if(self.type == "small_shadow") :
            #print("small start")
            self.small_shadow(point_up_y, point_down_y, point_up_y_right, point_down_y_right, offset_left, offset_right)
        elif(self.type == "middle_shadow") :
            #print("middle start")
            self.middle_shadow(point_up_y, point_down_y, point_up_y_right, point_down_y_right, offset_left, offset_right)
        else :
            #print("large start")
            self.large_shadow(point_up_y, point_down_y, point_up_y_right, point_down_y_right, offset_left, offset_right)

        #self.im_shadow = np.array(imread(self.img))
        #self.im2_shadow = np.array(imread(self.img))
        self.im_shadow = np.array(self.img)
        self.im2_shadow = np.array(self.img)
        self.height, self.width = self.im_shadow.shape[:2]

        l_l = self.inter_shadow(point_down_x[:], point_down_y[:])  # 왼쪽 아래, 세번째 인자 'cubic' 지움
        u_l = self.inter_shadow(point_up_x[:], point_up_y[:])  # 왼쪽 위
        l_r = self.inter_shadow(point_down_x_right[:], point_down_y_right[:])  # 오른쪽 아래
        u_r = self.inter_shadow(point_up_x_right[:], point_up_y_right[:])  # 오른쪽 위

        # 내 생각에는 범위 지정 느낌,,,
        for i in range(int(l_l[1][0]), int(l_l[1][-1] + 1)): # 303부터 431까지
            self.ext_shadow(u_l[0](i), l_l[0](i) + 1, i) # 여기서 error
            self.extleft_shadow(u_l[0](i), l_l[0](i) + 1, i)

        for i in range(int(l_r[1][0]), int(l_r[1][-1] + 1)):
            self.ext_shadow(u_r[0](i), l_r[0](i) + 1, i)
            self.extright_shadow(u_r[0](i), l_r[0](i) + 1, i)

        self.val = color.rgb2lab((self.im_shadow[self.x, self.y] / 255.).reshape(len(self.x), 1, 3)).reshape(len(self.x), 3)
        self.L_shadow = mean(self.val[:, 0])
        self.A_shadow = mean(self.val[:, 1])
        self.bB_shadow = mean(self.val[:, 2])

        rgbmean = (self.im_shadow[self.x, self.y])
        rmean = mean(rgbmean[:, 0])
        gmean = mean(rgbmean[:, 1])
        bmean = mean(rgbmean[:, 2])

        # rgb를 lab로 변경,,, 위의 내용과 다시 한 번 보기
        self.L_shadow, self.A_shadow, self.bB_shadow = color.rgb2lab(
            np.array((rmean / 255., gmean / 255., bmean / 255.)).reshape(1, 1, 3)).reshape(3, )
        self.L1_shadow, self.A1_shadow, self.B1_shadow = color.rgb2lab(np.array((self.R / 255., self.G / 255., self.B / 255.)).reshape(1, 1, 3)).reshape(3, )
        self.val[:, 0] += (self.L1_shadow - self.L_shadow)
        self.val[:, 1] += (self.A1_shadow - self.A_shadow)
        self.val[:, 2] += (self.B1_shadow - self.bB_shadow)


    def makeupFace_shadow_blending(self, inten):
        self.val[:, 0] -= (self.L1_shadow - self.L_shadow)
        self.val[:, 1] -= (self.A1_shadow - self.A_shadow)
        self.val[:, 2] -= (self.B1_shadow - self.bB_shadow)
        self.val[:, 0] += (self.L1_shadow - self.L_shadow) * inten
        self.val[:, 1] += (self.A1_shadow - self.A_shadow) * inten
        self.val[:, 2] += (self.B1_shadow - self.bB_shadow) * inten

    def shadow_makeup_finally(self):
        #image_blank = imread(self.img)  # Input.jpg 이미지 읽어와서 image_blank에 저장
        image_blank = self.img  # Input.jpg 이미지 읽어와서 image_blank에 저장
        #image_blank = imutils.resize(image_blank, width=1000)
        image_blank_copy = image_blank.copy()  # read-only를 대비한 copy값 생성
        image_blank_copy *= 0  # image_blank_copy 값을 0으로 만들기,,,? 근데 왜? 그럴 거면 imread 한 이유가 없음... python 에서 a = imul(a, b)는 a *= b와 동등. *= 뜻은 왼쪽 변수에 오른쪽 값을 곱하고 결과를 왼쪽변수에 할당
        image_blank_copy[self.x, self.y] = color.lab2rgb(self.val.reshape(len(self.x), 1, 3)).reshape(len(self.x), 3) * 255  # lab를 rgb로

        original = color.rgb2lab((self.im_shadow[self.x, self.y] * 0 / 255.).reshape(len(self.x), 1, 3)).reshape(len(self.x), 3)  # rgb를 lab로
        tobeadded = color.rgb2lab((image_blank_copy[self.x, self.y] / 255.).reshape(len(self.x), 1, 3)).reshape(len(self.x), 3)  # rgb를 lab로
        original += tobeadded
        self.im_shadow[self.x, self.y] = color.lab2rgb(original.reshape(len(self.x), 1, 3)).reshape(len(self.x), 3) * 255  # lab를 rgb로

        # Blur Filter
        filter = np.zeros((self.height, self.width))  # 모두 0으로 구성된 배열 생성
        cv2.fillConvexPoly(filter, np.array(c_[self.yleft, self.xleft], dtype='int32'),
                          1)  # 다각형 채우는 함수 cv2. fillConvexPoly ( img, points, color [ , lineType [ , shift ] ] ) → None
        cv2.fillConvexPoly(filter, np.array(c_[self.yright, self.xright], dtype='int32'),
                          1)  # 위와 이어짐. 또는 cv. FillConvexPoly ( img, pn, color, lineType=8, shift=0 ) → None

        filter = cv2.GaussianBlur(filter, (31, 31), 0)  # 이미지를 흐리게 해준다.

        # Erosion to reduce blur size 블러 크기를 줄이기 위한 침식
        kernel = np.ones((12, 12), np.uint8)
        filter = cv2.erode(filter, kernel,
                           iterations=1)  # 표준 수학적 형태 연산으로 이 함수는 표준 수학적 형태 연산을 제공하며, 이는 임의의 수의 차원으로 배열 데이터에 적용 할 수 있습니다. 이진 및 그레이 스케일 형태가 지원됩니다. erode(x, kernel)

        alpha = np.zeros([self.height, self.width, 3], dtype='float64')
        alpha[:, :, 0] = filter
        alpha[:, :, 1] = filter
        alpha[:, :, 2] = filter

        face = ((alpha * self.im_shadow + (1 - alpha) * self.im2_shadow).astype('uint8'))
        return face
        #imshow((alpha * self.im_shadow + (1 - alpha) * self.im2_shadow).astype('uint8'))

        #imsave(self.img+"output.jpg", (alpha * self.im_shadow + (1 - alpha) * self.im2_shadow).astype('uint8'))
        #show()


#def select_shadow_type(type): # small_shadow, middle_shadow, large_shadow
#    shadow_type = type
#    return type
'''
#shadow_type = select_shadow_type(input()) # input() 변경해야할듯
shadow_type = "middle_shadow"
face = './test_image/ex4.jpg'
path = '../frame/shadowArray.txt'
face = cv2.imread("test_image/white.png")
shadow_color = "0., 255., 0."
e = eyeshadow_class(27, 61, 104, shadow_type, face, path)
e.eyeshadow_makeup()
# 투명도 조절
e.makeupFace_shadow_blending(1.0)
result = e.shadow_makeup_finally()

cv2.imshow('result',result)
#cv2.imwrite('result_middle3.jpg',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
