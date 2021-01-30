from __future__ import division
import cv2
from scipy.interpolate import splprep, splev
from pylab import *
from skimage import color

class makeup(object):

    def __init__(self, img, file):
        """ Initiator method for class """
        self.red_l = 0
        self.green_l = 0
        self.blue_l = 0
        self.red_b = 0
        self.green_b = 0
        self.blue_b = 0
        self.image = img
        self.height, self.width = self.image.shape[:2]
        self.im_copy = self.image.copy()

        #self.intensity = 0.8

        self.x = []
        self.y = []
        self.xleft=[]
        self.yleft=[]
        self.xright=[]
        self.yright=[]

        file = np.loadtxt(file)
        self.points = np.floor(file)

    def __get_boundary_points_right(self, flag):

        points_1 = [self.points[0][0], self.points[0][1]]
        points_2 = [self.points[1][0], self.points[1][1]]
        points_3 = [self.points[2][0], self.points[2][1]]
        points_4 = [self.points[3][0], self.points[3][1]]
        points_5 = points_1

        #imsave('blush_output_.jpg', self.image)
        points = np.array([points_1, points_2, points_3, points_4, points_5])
        x, y = points[0:5, 0], points[0:5, 1]

        tck, u = splprep([x, y], s=0, per=1)
        unew = np.linspace(u.min(), u.max(), 1000)
        xnew, ynew = splev(unew, tck, der=0)
        tup = c_[xnew.astype(int), ynew.astype(int)].tolist()
        coord = list(set(tuple(map(tuple, tup))))
        coord = np.array([list(elem) for elem in coord])

        return np.array(coord[:, 0], dtype=np.int32), np.array(coord[:, 1], dtype=np.int32)

    def __get_boundary_points_left(self, flag):
        points_1 = [self.points[5][0], self.points[5][1]]
        points_2 = [self.points[8][0], self.points[8][1]]
        points_3 = [self.points[7][0], self.points[7][1]]
        points_4 = [self.points[6][0], self.points[6][1]]
        points_5 = points_1

        #imsave('blush_output_.jpg', self.image)

        points = np.array([points_1, points_2, points_3, points_4, points_5])

        x, y = points[0:5, 0], points[0:5, 1]

        tck, u = splprep([x, y], s=0, per=1)
        unew = np.linspace(u.min(), u.max(), 1000)
        xnew, ynew = splev(unew, tck, der=0)
        tup = c_[xnew.astype(int), ynew.astype(int)].tolist()
        coord = list(set(tuple(map(tuple, tup))))
        coord = np.array([list(elem) for elem in coord])

        return np.array(coord[:, 0], dtype=np.int32), np.array(coord[:, 1], dtype=np.int32)


    def __blush(self, x_right, y_right, x_left, y_left, intensity):

        # Create blush shape
        mask = np.zeros((self.height, self.width))
        cv2.fillConvexPoly(mask, np.array(c_[x_right, y_right], dtype='int32'), 1)
        cv2.fillConvexPoly(mask, np.array(c_[x_left, y_left], dtype='int32'), 1)
        mask = cv2.GaussianBlur(mask, (51, 51), 0) * intensity

        # Add blush color to image
        val = cv2.cvtColor(self.im_copy, cv2.COLOR_RGB2LAB).astype(float)
        val[:, :, 0] = val[:, :, 0] / 255. * 100.
        val[:, :, 1] = val[:, :, 1] - 128.
        val[:, :, 2] = val[:, :, 2] - 128.
        LAB = color.rgb2lab(np.array((self.red_b / 255., self.green_b / 255., self.blue_b / 255.)).reshape(1, 1, 3)).reshape(3,)

        mean_val = np.mean(np.mean(val, axis=0), axis = 0)
        mask = np.array([mask,mask,mask])
        mask = np.transpose(mask, (1,2,0))
        lab = np.multiply((LAB - mean_val), mask)

        val[:, :, 0] = np.clip(val[:, :, 0] + lab[:,:,0], 0, 100)
        val[:, :, 1] = np.clip(val[:, :, 1] + lab[:,:,1], -127, 128)
        val[:, :, 2] = np.clip(val[:, :, 2] + lab[:,:,2], -127, 128)

        self.im_copy = (color.lab2rgb(val) * 255).astype(np.uint8)


    def apply_blush(self, color, intensity):

        # Find Blush Loacations
        x_right, y_right = self.__get_boundary_points_right(0)
        x_left, y_left = self.__get_boundary_points_left(1)

        color_set = color.split(",")

        # Apply Blush
        self.red_b = float(color_set[0])
        self.green_b = float(color_set[1])
        self.blue_b = float(color_set[2])
        self.__blush(x_right, y_right, x_left, y_left, intensity)
        return self.im_copy

    def apply_makeup_all(self, color, inten):
        self.im_copy = self.apply_blush(color, inten)

        return self.im_copy
'''

#lip_color = "229., 172., 164."
shape = "square"
blusher_color = "105, 89, 240"
blusher_inten = 1.0
#file_path = 'test_2.txt'
file_path = "../frame/"+shape+"Blusher1.txt"
#img = io.imread('./data/test_four.jpg')
img = cv2.imread('./test_image/white.png')

m = makeup(img, file_path)
im = m.apply_makeup_all(blusher_color, blusher_inten)

plt.figure()
plt.imshow(im)
plt.show()


#im = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('result',im)
cv2.imwrite('square.png',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('test_2_output.jpg',im)


#import cv2
#im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
#cv2.imwrite('test_2_output.jpg',im)
'''