from pylab import *
from scipy.interpolate import interp1d
from skimage import color

class lipstick_class(object):

    def __init__(self, R, G, B, img, coordinate_value):
        self.r, self.g, self.b = R, G, B  # lipstick color

        #self.inten = inten
        self.up_left_end = 3
        self.up_right_end = 5
        self.img = img
        self.coordinate_value = coordinate_value
        self.x = []  # will contain the x coordinates of points on lips
        self.y = []  # will contain the y coordinates of points on lips
        self.point_out_x = []
        self.point_out_y = []
        self.point_in_x = []
        self.point_in_y = []


    def inter(self, lx, ly, k1='quadratic'): # 보간법을 적용하여 linear(선형보정) quadratic(부드러운 보정) 두가지 방법
        #print("실행됨")
        unew = np.arange(lx[0], lx[-1] + 1, 1)
        f2 = interp1d(lx, ly, kind=k1, bounds_error = False, fill_value = 'extrapolate')
        return f2, unew

    def lipstick_makeup(self):
        # gets the points on the boundary of lips from the file
        file = np.loadtxt(self.coordinate_value)
        points = np.floor(file)
        self.point_out_x = np.array((points[:len(points) // 2][:, 0]))
        self.point_out_y = np.array(points[:len(points) // 2][:, 1])
        self.point_in_x = (points[len(points) // 2:][:, 0])
        self.point_in_y = points[len(points) // 2:][:, 1]

        #figure()
        #self.im = imread(self.img)
        self.im = self.img
        #self.im = imutils.resize(self.im, width=1000)

        # Code for the curves bounding the lips
        o_u_l = self.inter(self.point_out_x[:self.up_left_end], self.point_out_y[:self.up_left_end])
        o_u_r = self.inter(self.point_out_x[self.up_left_end - 1:self.up_right_end], self.point_out_y[self.up_left_end - 1:self.up_right_end])
        o_l = self.inter([self.point_out_x[0]] + self.point_out_x[self.up_right_end - 1:][::-1].tolist(),
                    [self.point_out_y[0]] + self.point_out_y[self.up_right_end - 1:][::-1].tolist(), 'cubic')
        i_u_l = self.inter(self.point_in_x[:self.up_left_end], self.point_in_y[:self.up_left_end])
        i_u_r = self.inter(self.point_in_x[self.up_left_end - 1:self.up_right_end], self.point_in_y[self.up_left_end - 1:self.up_right_end])
        i_l = self.inter([self.point_in_x[0]] + self.point_in_x[self.up_right_end - 1:][::-1].tolist(),
                    [self.point_in_y[0]] + self.point_in_y[self.up_right_end - 1:][::-1].tolist(), 'cubic')


        def ext(a, b, i):
            a, b = np.round(a), np.round(b)
            self.x.extend(arange(a, b, 1, dtype=np.int32).tolist())
            self.y.extend((ones(int(b - a), dtype=np.int32) * i).tolist())

        for i in range(int(o_u_l[1][0]), int(i_u_l[1][0] + 1)):
            ext(o_u_l[0](i), o_l[0](i) + 1, i)

        for i in range(int(i_u_l[1][0]), int(o_u_l[1][-1] + 1)):
            ext(o_u_l[0](i), i_u_l[0](i) + 1, i)
            ext(i_l[0](i), o_l[0](i) + 1, i)
        for i in range(int(i_u_r[1][-1]), int(o_u_r[1][-1] + 1)):
            ext(o_u_r[0](i), o_l[0](i) + 1, i)

        for i in range(int(i_u_r[1][0]), int(i_u_r[1][-1] + 1)):
            ext(o_u_r[0](i), i_u_r[0](i) + 1, i)
            ext(i_l[0](i), o_l[0](i) + 1, i)

        # Now x and y contains coordinates of all the points on lips

        self.val = color.rgb2lab((self.im[self.x, self.y] / 255.).reshape(len(self.x), 1, 3)).reshape(len(self.x), 3)

        L, A, B = mean(self.val[:, 0]), mean(self.val[:, 1]), mean(self.val[:, 2])
        L1, A1, B1 = color.rgb2lab(np.array((self.r / 255., self.g / 255., self.b / 255.)).reshape(1, 1, 3)).reshape(3, )
        self.ll, self.aa, self.bb = L1 - L, A1 - A, B1 - B
        self.val[:, 0] += self.ll
        self.val[:, 1] += self.aa
        self.val[:, 2] += self.bb

#    def makeupFace_lip_fill(self):
#        self.val[:, 0] += self.ll
#        self.val[:, 1] += self.aa
#        self.val[:, 2] += self.bb


    def makeupFace_lip_blending(self, inten) :
        self.val[:, 0] -= self.ll
        self.val[:, 1] -= self.aa
        self.val[:, 2] -= self.bb
        self.val[:, 0] += self.ll * inten
        self.val[:, 1] += self.aa * inten
        self.val[:, 2] += self.bb * inten


    def lip_makeup_finally(self) :
        im2 = self.im.copy()

        im2[self.x, self.y] = color.lab2rgb(self.val.reshape(len(self.x), 1, 3)).reshape(len(self.x), 3) * 255

        gca().set_aspect('equal', adjustable='box')

        return im2
        #imshow(im2)
        #show()
        #imsave(self.img+'outputtest.jpg', im2)
import cv2
'''
face = '../capture.jpg'

file_path = '../frame/lipsArray.txt'
face = imread('../capture.jpg')
l = lipstick_class(249., 107., 125., face, file_path)
l.lipstick_makeup()
# 투명도 조절
l.makeupFace_lip_blending(1.0)
result = l.lip_makeup_finally()
result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''




