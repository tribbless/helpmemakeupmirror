import imutils
import numpy as np
import cv2
import dlib

class EyeLiner:
    def __init__(self, name):
        self.name = name

    def frame(self, image, shape, colors=(255, 69, 69), alpha=0.75):
        image = Liner(image, shape, False, self.name, colors)
        image = Liner(image, shape, True, self.name, colors)
        return image


def SetLinerTemp(startP, shape):
    temp = shape[startP:startP + 6]
    return temp


def Liner(image, shape, isRight, name, colors=None, alpha=0.75):
    newP = np.zeros((1, 2), dtype="int")
    landmark = np.zeros((1, 2), dtype="int")
    landmark2 = np.zeros((1, 2), dtype="int")
    if isRight:
        temp = SetLinerTemp(42, shape)
        landmark = temp[3]
        landmark2 = temp[2]
        newP[0][0] = temp[3][0] + abs((temp[0][0] - temp[3][0]) / 4)

    else:  # left
        temp = SetLinerTemp(36, shape)
        landmark = temp[0]
        landmark2 = temp[1]
        newP[0][0] = temp[0][0] - abs((temp[0][0] - temp[3][0]) / 4)

    if name == "Middle":
        newP[0][1] = landmark[1]
    elif name == "Up":
        newP[0][1] = landmark2[1] + abs(landmark2[1] - landmark[1]) * 2 / 3
    # right x : 46x + abs((43x - 46x)/5) : temp3 ,0
    # right y : 46번의 좌표와 같다

    numm = 2
    dx = abs((landmark[0] - newP[0][0])) / numm
    dy = abs((landmark[1] - newP[0][1])) / numm
    f = np.zeros((numm + 1, 2), dtype="int")
    if isRight == False:  dx *= -1
    for i in range(numm + 1):
        f[i][0] = landmark[0] + dx * i
        f[i][1] = landmark[1] - dy * i

    draw_frame_liner(f, image, colors)

    return image


class EyeShadow:
    def __init__(self, name="Middle"):
        self.name = name

    def frame(self, image, shape, colors=(51, 255, 204), alpha=0.75):
        kind = 0
        if (self.name == "Large"):
            kind = 1
        if (self.name == "Small"):
            kind = -1
        image = Shadow(image, shape, kind, colors)
        return image


def Shadow(image, shape, kind, colors=None, alpha=0.75):
    tempRight = shape[42: 48]
    tempLeft = shape[36:42]

    testEyeLeft = shape[36:42]
    testEyeRight = shape[42:48]

    coordinate_value = "frame/shadowArray.txt"
    file_shadow = np.loadtxt(coordinate_value)
    lower_left_end = 5  # 5번째 left의 마지막꺼 11개 있는데 5개
    upper_left_end = 11
    lower_right_end = 16
    upper_right_end = 22

    points = np.floor(file_shadow)
    point_down_x = np.array((points[:lower_left_end][:, 0]))
    point_down_y = np.array(points[:lower_left_end][:, 1])
    point_up_x = np.array(points[lower_left_end:upper_left_end][:, 0])
    point_up_y = np.array(points[lower_left_end:upper_left_end][:, 1])
    point_down_x_right = np.array((points[upper_left_end:lower_right_end][:, 0]))
    point_down_y_right = np.array(points[upper_left_end:lower_right_end][:, 1])
    point_up_x_right = np.array((points[lower_right_end:upper_right_end][:, 0]))
    point_up_y_right = np.array(points[lower_right_end:upper_right_end][:, 1])

    point_down_y_max = max(point_down_y)
    point_up_y_min = min(point_up_y)
    offset_left = point_down_y_max - point_up_y_min

    point_down_y_right_max = max(point_down_y_right)
    point_up_y_right_min = min(point_up_y_right)
    offset_right = point_down_y_right_max - point_up_y_right_min

    if kind == 0:  # middle 중간
        point_up_y[0] += offset_left * 0.625
        point_up_y[1] += offset_left * 0.51
        point_up_y[2] += offset_left * 0.36
        point_up_y[3] += offset_left * 0.31
        point_up_y[4] += offset_left * 0.41

        point_up_y_right[-1] += offset_right * 0.625
        point_up_y_right[1] += offset_right * 0.41
        point_up_y_right[2] += offset_right * 0.31
        point_up_y_right[3] += offset_right * 0.351
        point_up_y_right[4] += offset_right * 0.51
    elif kind == 1:  # large 넓은 영역
        point_up_y[0] += offset_left * 0.525
        point_up_y[1] += offset_left * 0.31
        point_up_y[2] += offset_left * 0.26
        point_up_y[3] += offset_left * 0.21
        point_up_y[4] += offset_left * 0.31

        point_up_y_right[-1] += offset_right * 0.525
        point_up_y_right[1] += offset_right * 0.31
        point_up_y_right[2] += offset_right * 0.21
        point_up_y_right[3] += offset_right * 0.251
        point_up_y_right[4] += offset_right * 0.41
    elif kind == -1:  # small 좁은 영역
        point_up_y[0] += offset_left * 0.725
        point_up_y[1] += offset_left * 0.51
        point_up_y[2] += offset_left * 0.46
        point_up_y[3] += offset_left * 0.41
        point_up_y[4] += offset_left * 0.51

        point_up_y_right[-1] += offset_right * 0.725
        point_up_y_right[1] += offset_right * 0.51
        point_up_y_right[2] += offset_right * 0.41
        point_up_y_right[3] += offset_right * 0.451
        point_up_y_right[4] += offset_right * 0.51

    lfup = np.zeros((point_up_x.size, 2), dtype="int")
    lfup = setShadowFrame(point_up_x, point_up_y, lfup)
    lfup[0][0] = abs((lfup[0][0] - lfup[1][0])/2) + lfup[0][0]
    lfup[0][1] = lfup[0][1] - abs((lfup[0][1] - lfup[1][1])/2)
    image = draw_frame(lfup[:-1], image, colors)

    rfup = np.zeros((point_up_x_right.size, 2), dtype="int")
    rfup = setShadowFrame(point_up_x_right, point_up_y_right, rfup)
    rfup[-1][0] = rfup[-1][0] - abs((rfup[-1][0] - rfup[-2][0])/2)
    rfup[-1][1] = rfup[-1][1] - abs((rfup[-1][1] - rfup[-2][1])/2)
    image = draw_frame(rfup[1:], image, colors)

    return image


def setShadowFrame(point_x, point_y, frame):
    for i in range(point_x.size):
        frame[i][0] = point_x[i]
        frame[i][1] = point_y[i]
    return frame


class EyeBrow:
    captureArr = 0

    def __init__(self, name="Arch"):
        self.name = name

    def frame(self, image, shape, forShadow=False, customize=(False, "round"), colors=(218, 255, 48),  flag=0,
              alpha=0.75, num=9):
        if self.name == "Straight":
            image_arr_left = StraightFrame(image, shape, num, 17, False, colors)  # left
            image_arr_right = StraightFrame(image, shape, num, 22, True, colors)  # right
            self.captureArr = (image_arr_right[1], image_arr_left[1])
            image = image_arr_right[0]
        elif self.name == "Arch":
            image_arr_left = ArchFrame(image, shape, num, 17, False, forShadow, customize, colors, flag)  # left
            image_arr_right = ArchFrame(image, shape, num, 22, True, forShadow, customize, colors, flag)  # right
            self.captureArr = (image_arr_right[1], image_arr_left[1])
            image = image_arr_right[0]

        return image

def between_eye(shape):
    eye_left = abs(shape[36][0] - shape[39][0])
    eye_between = abs(shape[39][0] - shape[42][0])
    value = eye_between / eye_left
    result = "normal"  # 보통 미간
    if value > 1.63:
        result = "wide"  # 넓은 미간
    elif value < 1.53:
        result = "narrow"  # 좁은 미간

    return result

def ArchFrame(image, shape, num, startPi, isRight, forShadow, customize, colors=None, flag=0, alpha=0.75):
    temp = setTemp(isRight, shape, startPi, 5)  # 왼쪽은 temp[0]이 22번
    d = 10

    benchmark = np.zeros((3, 2), dtype="int")

    benchmark[0][0] = temp[0][0]
    benchmark[0][1] = temp[0][1] + d
    if benchmark[0][1] > temp[4][1]:
        benchmark[1][1] = temp[2][1] + int(abs(temp[0][1] + d - temp[2][1]) / 2)
    else:
        benchmark[1][1] = temp[2][1] + int(abs(temp[4][1] - temp[2][1]) / 2)
    benchmark[2][1] = temp[3][1] + int(abs((temp[3][1] - temp[4][1]) / 2))

    if isRight == False:
        benchmark[1][0] = temp[1][0] - int(abs(temp[1][0] - temp[2][0])) * 2 / 3
        benchmark[2][0] = benchmark[1][0] - int(abs(benchmark[1][0] - temp[4][0])) / 2
    else:
        benchmark[1][0] = temp[1][0] + int(abs(temp[1][0] - temp[2][0])) * 2 / 3
        benchmark[2][0] = benchmark[1][0] + int(abs(benchmark[1][0] - temp[4][0])) / 2

    # 눈썹 아래쪽 프레임 1 to 2
    numm = 4
    db_x1 = abs((benchmark[1][0] - benchmark[0][0])) / numm
    db_y1 = abs((benchmark[1][1] - benchmark[0][1])) / numm
    bf1 = np.zeros((numm + 1, 2), dtype="int")
    if isRight == False:  db_x1 *= -1
    for i in range(numm + 1):
        bf1[i][0] = benchmark[0][0] + db_x1 * i
        bf1[i][1] = benchmark[0][1] - db_y1 * i

    # 눈썹 아래쪽 프레임 2 to 3
    pb2 = abs(int((benchmark[1][0] - benchmark[2][0]) / db_x1))
    db_x2 = abs((benchmark[1][0] - benchmark[2][0])) / pb2
    db_y2 = abs((benchmark[1][1] - benchmark[2][1])) / pb2
    bf2 = np.zeros((pb2, 2), dtype="int")
    if isRight == False:  db_x2 *= -1
    for i in range(pb2):
        bf2[i][0] = benchmark[1][0] + db_x2 * i
        bf2[i][1] = benchmark[1][1] - db_y2 * i

    nTemp = np.zeros((1, 2), dtype="int")
    ntf1 = ntf2 = ntf3 = ntf4 = 0
    if customize[0]:
        #미간 고려
        Glabella = between_eye(shape)  # 미간
        right = 1
        if not isRight:
            right = -1

        if Glabella == "wide":  # 나는 미간이 넓어요
            nTemp[0][0] = temp[1][0] + right * (int(abs(temp[2][0] - temp[1][0]) / 2))
        elif Glabella == "narrow":  # 나느 미간이 좁아요
            nTemp[0][0] = temp[2][0] + right * (int(abs(temp[3][0] - temp[2][0]) / 2))
        else:  # 나는 보통의 미간
            nTemp[0][0] = temp[2][0]  # x

        if customize[1] == "square":
            # 각진 얼굴형일 때 사용할 코드
            nTemp[0][1] = temp[2][1]
        elif customize[1] == "round":
            # 둥근 얼굴형일 때 사용할 코드
            nTemp[0][1] = temp[2][1] - abs(int(db_x1 / 2))  # y

        # new tf
        ntf1 = SetArchTop(db_x1, temp[0], temp[1], True, False, isRight)
        ntf2 = SetArchTop(db_x1, temp[1], nTemp[0], True, False, isRight)
        ntf3 = SetArchTop(db_x1, nTemp[0], temp[3], False, False, isRight)
        ntf4 = SetArchTop(db_x1, temp[3], temp[4], False, True, isRight)

    # 눈썹 위쪽 프레임
    tf1 = SetArchTop(db_x1, temp[0], temp[1], True, False, isRight)
    tf2 = SetArchTop(db_x1, temp[1], temp[2], True, False, isRight)
    tf3 = SetArchTop(db_x1, temp[2], temp[3], False, False, isRight)
    tf4 = SetArchTop(db_x1, temp[3], temp[4], False, True, isRight)

    # 눈썹 아래쪽 프레임 3 to 27
    pb3 = abs(int((benchmark[2][0] - tf4[-1][0]) / db_x1)) + 1
    db_x3 = abs((benchmark[2][0] - tf4[-1][0])) / pb3
    db_y3 = abs((benchmark[2][1] - tf4[-1][1])) / pb3
    bf3 = np.zeros((pb3, 2), dtype="int")
    if isRight == False:  db_x3 *= -1
    if benchmark[2][1] > tf4[-1][1]: db_y3 *= -1
    for i in range(pb3):
        bf3[i][0] = benchmark[2][0] + db_x3 * i
        bf3[i][1] = benchmark[2][1] + db_y3 * i

    shadow_left = np.zeros((11, 2), dtype="int")
    shadow_right = np.zeros((11, 2), dtype="int")
    # 쉐도우영역 배열 생성
    if forShadow == True:
        if (isRight == False):  # left
            shadow_left[0] = shape[17]
            shadow_left[1:5] = shape[36:40]
            shadow_left[5] = shape[17]
            shadow_left[6] = tf4[-2]
            shadow_left[7] = tf3[-1]
            shadow_left[8] = tf2[-1]
            shadow_left[9][0] = tf2[-1][0] + abs(shape[39][0] - shape[38][0])
            shadow_left[9][1] = tf1[-1][1]
            shadow_left[10] = shape[39]
            shadow_left = DeleteErrorArray(5, 10, shadow_left)
            shadow_left = DeleteErrorArray(0, 4, shadow_left)
            if flag == 1:
                makeTxtFile(shadow_left, "frame/shadowArray2.txt", "w")
            else:
                makeTxtFile(shadow_left, "frame/shadowArray.txt", "w")
        else:  # right
            shadow_right[0:4] = shape[42:46]
            shadow_right[4] = shape[26]
            shadow_right[5] = shape[42]
            shadow_right[6:11] = shape[22:27]
            shadow_right = DeleteErrorArray(0, 4, shadow_right)
            shadow_right = DeleteErrorArray(5, 10, shadow_right)
            if flag == 1:
                makeTxtFile(shadow_right, "frame/shadowArray2.txt", "a")
            else:
                makeTxtFile(shadow_right, "frame/shadowArray.txt", "a")
    else:

        draw_frame(bf1, image, colors)
        draw_frame(bf2, image, colors)
        draw_frame(bf3, image, colors)

        if customize[0]:
            # 맞춤형으로 그려줄 때
            draw_frame(ntf1, image, colors)
            draw_frame(ntf2, image, colors)
            draw_frame(ntf3, image, colors)
            draw_frame(ntf4, image, colors)
        else:
            # 평범한거 그릴때
            draw_frame(tf1, image, colors)
            draw_frame(tf2, image, colors)
            draw_frame(tf3, image, colors)
            draw_frame(tf4, image, colors)

    captureArr = (bf1, bf2, bf3, tf1, tf2, tf3, tf4)
    return image, captureArr


def DeleteErrorArray(start, finish, shadow_dir):
    for i in range(start, finish):
        if shadow_dir[i][0] > shadow_dir[i + 1][0]:  # index 5와 6 비교 5값이 더 크면 6값을 5로 바꾸고 1더해줌, index 10
            shadow_dir[i + 1][0] = shadow_dir[i][0] + 1
    return shadow_dir


def SetArchTop(db_x1, temp1, temp2, isUp, is27, isRight):
    pt = abs(int((temp2[0] - temp1[0]) / db_x1))
    if is27 == True: pt += 2
    dt_x = abs((temp2[0] - temp1[0])) / pt
    dt_y = abs((temp2[1] - temp1[1])) / pt
    tf = np.zeros((pt, 2), dtype="int")
    if isUp == False: dt_y *= -1
    if isRight == False: dt_x *= -1
    for i in range(pt):
        tf[i][0] = temp1[0] + dt_x * i
        tf[i][1] = temp1[1] - dt_y * i
    return tf


def StraightFrame(image, shape, num, startPi, isRight, colors=None, alpha=0.75):
    temp = setTemp(isRight, shape, startPi, 5)

    # 눈썹 아래쪽 프레임
    db_x = (temp[4][0] - temp[0][0]) / num
    bf = np.zeros((num + 1, 2), dtype="int")

    for i in range(num + 1):
        bf[i][1] = temp[0][1]
        bf[i][0] = temp[0][0] + db_x * i

    # 눈썹 위쪽 프레임
    pt = int(abs(bf[int(num * 2 / 3)][0] - temp[0][0]) / abs(db_x)) + 2  # 점찍을 개수 == 6 , top,bottom은 처음과 마지막을 찍어준다.
    tf = np.zeros((pt, 2), dtype="int")  # 6개의 배열
    dt_x = abs(bf[int(num * 2 / 3)][0] - temp[0][0]) / (pt - 1)  ## 길이에서 점들 사이의 차이 값

    if (isRight == False): dt_x *= -1.0

    # 24, 24, 26 세개의 temp 점들의 y값을 비교하여, 가운데 값을 찾아서 그 높이로 맞춰봄.
    a = temp[1]
    b = temp[2]
    c = temp[3]
    middle = (b if b[1] > c[1] else (c if a[1] > c[1] else a)) if a[1] > b[1] else (
        b if b[1] < c[1] else (a if a[1] > c[1] else c))

    for i in range(pt):
        tf[i][1] = middle[1]
        tf[i][0] = temp[0][0] + dt_x * i

    # 눈썹 측면 프레임
    pr = int(abs(tf[pt - 1][0] - bf[num][0]) / abs(db_x))
    dr_x = abs(tf[pt - 1][0] - bf[num][0]) / (pr + 1)
    dr_y = abs(tf[pt - 1][1] - bf[num][1]) / (pr + 1)
    sf = np.zeros((pr, 2), dtype="double")

    if (isRight == False): dr_x *= -1.0

    for i in range(int(pr / 2)):
        sf[i][0] = tf[pt - 1][0] + dr_x * (i + 1)
        sf[i][1] = tf[pt - 1][1] + dr_y * (i + 1) - (dr_y / 3) * (i + 1)
        sf[pr - 1 - i][0] = tf[pt - 1][0] + dr_x * (pr - 1 - i + 1)  # i자리에 pr-1-i 라는 index 값 넣어줌
        sf[pr - 1 - i][1] = tf[pt - 1][1] + dr_y * (pr - 1 - i + 1) - (dr_y / 3) * (i + 1)

    if (pr % 2 == 1):  # int(pr/2)+1 == 가운데 index
        sf[int(pr / 2)][0] = tf[pt - 1][0] + dr_x * (int(pr / 2) + 1)
        sf[int(pr / 2)][1] = tf[pt - 1][1] + dr_y * (int(pr / 2) + 1) - (dr_y / 3) * (int(pr / 2) + 1)

    draw_frame(bf, image, colors)
    draw_frame(tf, image, colors)
    draw_frame(sf, image, colors)
    captureArr = (bf, tf, sf)
    return image, captureArr


class Blusher:
    def __init__(self, name):
        self.name = name

    def frame(self, image, shape, colors=(51, 255, 204), flag=0, alpha=0.75):
        if (self.name == "Round"):
            image = RoundBlusher(image, shape, True, 13, colors, flag)  # right
            image = RoundBlusher(image, shape, False, 0, colors, flag)  # left
        elif (self.name == "Oblong"):
            image = OblongBlusher(image, shape, True, 13, colors, flag)  # right
            image = OblongBlusher(image, shape, False, 0, colors, flag)  # left
        elif (self.name == "Square"):
            image = SquareBlusher(image, shape, True, colors, flag)  # 오른쪽
            image = SquareBlusher(image, shape, False, colors, flag)  # 왼쪽
        return image


def DrawBlusher(op1, op2, point1, point2, dx, dy, isOblong):
    if (isOblong):
        dx = abs(point1[0] - point2[0]) / 3
        dy = abs(point1[1] - point2[1]) / 3

    p = int(abs(point1[1] - point2[1]) / dy) - 1
    f = np.zeros((p, 2), dtype="int")

    for i in range(int(p / 2)):
        f[i][0] = point1[0] + dx * (i + 1) * op1 + (dx / 3) * (i + 1) * op2
        f[i][1] = point1[1] + dy * (i + 1)
        f[p - 1 - i][0] = point1[0] + dx * (p - 1 - i + 1) * op1 + (dx / 3) * (i + 1) * op2
        f[p - 1 - i][1] = point1[1] + dy * (p - 1 - i + 1)
        if (p % 2 == 1):  # int(p/2)+1 == 가운데 index
            f[int(p / 2)][0] = point1[0] + dx * (int(p / 2) + 1) * op1 + (dx / 3) * (int(p / 2) + 1) * op2
            f[int(p / 2)][1] = point1[1] + dy * (int(p / 2) + 1)
    return f


def RoundBlusher(image, shape, isRight, startPi, colors=(51, 255, 204), flag=0, alpha=0.75, op=1):
    # set benchmark 3
    temp = setTemp(isRight, shape, startPi, 4, "roundBlusher")
    # setTemp 는 눈썹 전용으로 만들었던거라서  오른쪽 먼저 했었는데 블러셔는 왼쪽기준으로 먼저해서 그냥 바꿔서
    benchmark = np.zeros((5, 2), dtype="int")

    if isRight: op = -1

    benchmark[0][0] = temp[1][0] + op * abs(temp[0][1] - temp[1][1]) / 2  # A.x
    benchmark[0][1] = temp[0][1] + abs(temp[0][1] - temp[1][1]) / 2  # A.y
    benchmark[1][0] = temp[2][0] + op * abs(temp[2][0] - shape[27][0]) / 2  # B.x
    benchmark[1][1] = temp[2][1]  # B.y
    benchmark[2][0] = temp[2][0] + op * abs(temp[2][0] - benchmark[1][0]) / 2  # C.x
    benchmark[2][1] = temp[3][1]  # C.y
    benchmark[3] = temp[1]
    benchmark[4] = temp[2]

    p0 = 1
    f0 = np.zeros((p0, 2), dtype="int")
    f0[0][0] = temp[1][0] + op * abs(temp[1][0] - benchmark[0][0]) / 2
    f0[0][1] = temp[1][1] - abs(temp[1][1] - benchmark[0][1]) / 2
    dx = abs(temp[1][0] - benchmark[0][0]) / (p0 + 1)
    dy = abs(temp[1][1] - benchmark[0][1]) / (p0 + 1)

    f1 = DrawBlusher(op, op, benchmark[0], benchmark[1], dx, dy, False)
    f2 = DrawBlusher(-op, op, benchmark[1], benchmark[2], dx, dy, False)
    f3 = DrawBlusher(op, -op, temp[2], benchmark[2], dx, dy, False)

    # 블러셔 수인이에게 전달할 배열
    Blusher_left = np.zeros((5, 2), dtype="int")
    Blusher_right = np.zeros((5, 2), dtype="int")

    if isRight:
        Blusher_right[0] = benchmark[1]
        Blusher_right[1][0] = shape[16][0] - abs(shape[16][0] - shape[15][0]) / 2
        Blusher_right[1][1] = shape[16][1] + abs(shape[16][1] - shape[15][1]) / 2
        Blusher_right[2] = benchmark[4]
        Blusher_right[3] = f2[-1]
        Blusher_right[4] = Blusher_right[0]
        if flag == 1:
            makeTxtFile(Blusher_right, "frame/roundBlusher2.txt", "w")
        else:
            makeTxtFile(Blusher_right, "frame/roundBlusher.txt", "w")
    else:
        Blusher_left[0] = benchmark[1]
        Blusher_left[1] = f2[-1]
        Blusher_left[2] = benchmark[4]
        Blusher_left[3][0] = shape[0][0] + abs(shape[0][0] - shape[1][0]) / 2
        Blusher_left[3][1] = shape[0][1] + abs(shape[0][1] - shape[1][1]) / 2
        Blusher_left[4] = Blusher_left[0]
        if flag == 1:
            makeTxtFile(Blusher_left, "frame/roundBlusher2.txt", "a")
        else:
            makeTxtFile(Blusher_left, "frame/roundBlusher.txt", "a")

    image = draw_frame(benchmark, image, colors)
    image = draw_frame(f0, image, colors)
    image = draw_frame(f1, image, colors)
    image = draw_frame(f2, image, colors)
    image = draw_frame(f3, image, colors)

    return image


def OblongBlusher(image, shape, isRight, startPi, colors=(51, 255, 204), flag=0, alpha=0.75, op=1):
    temp = setTemp(isRight, shape, startPi, 4, "oblongBlusher")
    benchmark = np.zeros((5, 2), dtype="int")
    bp = np.zeros((1, 2), dtype="int")

    if isRight: op = -1
    benchmark[0] = temp[1]
    benchmark[1][0] = temp[2][0] + op * abs(temp[2][0] - temp[3][0]) / 3
    benchmark[1][1] = temp[2][1] + abs(temp[2][1] - temp[3][1]) / 3

    bp[0][0] = benchmark[0][0] + op * abs(benchmark[0][0] - shape[27][0]) / 2
    bp[0][1] = benchmark[0][1] + abs(benchmark[0][1] - temp[2][1]) / 2

    benchmark[2][0] = bp[0][0] + op * abs(bp[0][0] - shape[27][0]) / 3
    benchmark[2][1] = bp[0][1]
    benchmark[3][0] = benchmark[0][0] + op * abs(benchmark[0][0] - benchmark[2][0]) / 2
    benchmark[3][1] = benchmark[0][1] + abs(benchmark[0][1] - benchmark[2][1]) / 3
    benchmark[4][0] = benchmark[1][0] + op * abs(benchmark[1][0] - benchmark[2][0]) / 2
    benchmark[4][1] = benchmark[1][1] - abs(benchmark[1][1] - benchmark[2][1]) / 3

    # 블러셔 수인이에게 전달할 배열
    Blusher_left = np.zeros((5, 2), dtype="int")
    Blusher_right = np.zeros((5, 2), dtype="int")
    if isRight:
        Blusher_right[0][0] = benchmark[2][0]
        Blusher_right[0][1] = benchmark[2][1]
        Blusher_right[1][0] = benchmark[3][0] + abs(benchmark[0][0] - benchmark[3][0]) / 2
        Blusher_right[1][1] = benchmark[3][1]
        Blusher_right[2][0] = benchmark[1][0]
        Blusher_right[2][1] = benchmark[2][1]
        Blusher_right[3][0] = Blusher_right[1][0]
        Blusher_right[3][1] = benchmark[4][1]
        Blusher_right[4] = Blusher_right[0]
        if flag == 1:
            makeTxtFile(Blusher_right, "frame/oblongBlusher2.txt", "w")
        else:
            makeTxtFile(Blusher_right, "frame/oblongBlusher.txt", "w")
    else:
        Blusher_left[0][0] = benchmark[2][0]
        Blusher_left[0][1] = benchmark[2][1]
        Blusher_left[1][1] = benchmark[4][1]
        Blusher_left[2][0] = benchmark[1][0]
        Blusher_left[2][1] = benchmark[2][1]
        Blusher_left[3][0] = benchmark[0][0] + abs(benchmark[0][0] - benchmark[3][0]) / 2
        Blusher_left[1][0] = Blusher_left[3][0]
        Blusher_left[3][1] = benchmark[3][1]
        Blusher_left[4] = Blusher_left[0]
        if flag == 1:
            makeTxtFile(Blusher_left, "frame/oblongBlusher2.txt", "a")
        else:
            makeTxtFile(Blusher_left, "frame/oblongBlusher.txt", "a")

    f0 = DrawBlusher(op, op, benchmark[0], benchmark[3], 0, 0, True)
    f1 = DrawBlusher(op, op, benchmark[3], benchmark[2], 0, 0, True)
    f2 = DrawBlusher(-op, op, benchmark[2], benchmark[4], 0, 0, True)
    f3 = DrawBlusher(-op, op, benchmark[4], benchmark[1], 0, 0, True)

    image = draw_frame(f0, image, colors)
    image = draw_frame(f1, image, colors)
    image = draw_frame(f2, image, colors)
    image = draw_frame(f3, image, colors)
    image = draw_frame(benchmark, image, colors)
    return image


def setTemp(isRight, shape, startPi, addi, forWhat="eyebrow"):
    if forWhat != "eyebrow":
        if isRight:
            isRight = False
        else:
            isRight = True
        # round blusher 를 왼쪽 기준으로 생성 해버려서 temp 해줄 때 is left일때 reverse 안해줌 ㅜㅠㅠ 잘 못 짰다.
    if isRight:
        temp = shape[startPi: startPi + addi]
    else:
        tempReverse = shape[startPi: startPi + addi]
        temp = tempReverse[::-1]
    return temp


def SquareBlusher(image, shape, isRight, colors=(51, 255, 204), flag=0, alpha=0.75):
    up = [0, 0]
    down = [0, 0]
    final = [0, 0]
    end_up = [0, 0]
    end_down = [0, 0]
    middle_up = [0, 0]
    middle_down = [0, 0]
    thickness = 2  # 두께 설정 동그라미 그리는 거

    if isRight:
        up[0] = shape[14][0]
        down[0] = shape[13][0] - abs(shape[12][0] - shape[13][0]) * 0.5
        middle_up[0] = shape[45][0]  # 46번점 x좌표
        end_up[0] = shape[46][0] - abs((shape[46][0] - shape[47][0]) / 2)
        final[0] = shape[47][0]
    else:
        up[0] = shape[2][0]
        down[0] = shape[3][0] + abs(shape[3][0] - shape[4][0]) * 0.5
        middle_up[0] = shape[36][0]  # 37번점 x좌표
        end_up[0] = abs((shape[40][0] - shape[41][0]) / 2) + shape[41][0]
        final[0] = shape[40][0]

    middle_down[0] = middle_up[0]
    end_down[0] = end_up[0]

    up[1] = shape[41][1] + abs(shape[41][1] - shape[48][1]) * 0.1
    down[1] = shape[41][1] + abs(shape[41][1] - shape[48][1]) * 0.75

    middle_up[1] = shape[41][1] + abs(shape[41][1] - shape[48][1]) * 0.17
    middle_down[1] = shape[41][1] + abs(shape[41][1] - shape[48][1]) * 0.68

    end_up[1] = shape[41][1] + abs(shape[41][1] - shape[48][1]) * 0.26
    end_down[1] = shape[41][1] + abs(shape[41][1] - shape[48][1]) * 0.57

    final[1] = abs((end_up[1] - end_down[1]) / 2) + end_up[1]
    # 블러셔 텍스트 파일용 배열 생성
    Blusher_left = np.zeros((5, 2), dtype="int")
    Blusher_right = np.zeros((5, 2), dtype="int")
    if isRight:
        Blusher_right[0][0] = final[0]
        Blusher_right[0][1] = abs((final[1] - end_up[1]) / 2) + final[1]
        Blusher_right[1][0] = middle_up[0] + abs(middle_up[0] - up[0]) * 0.67
        Blusher_right[1][1] = middle_up[1] + abs(middle_up[1] - final[1]) * 0.07
        Blusher_right[2][0] = up[0]
        Blusher_right[2][1] = final[1]
        Blusher_right[3][0] = Blusher_right[1][0]
        Blusher_right[3][1] = final[1] + abs(final[1] - Blusher_right[1][1])
        Blusher_right[4] = Blusher_right[0]
        if flag == 1:
            makeTxtFile(Blusher_right, "frame/squareBlusher2.txt", "w")
        else:
            makeTxtFile(Blusher_right, "frame/squareBlusher.txt", "w")
    else:
        Blusher_left[0][0] = final[0]
        Blusher_left[0][1] = abs((final[1] - end_up[1]) / 2) + final[1]
        Blusher_left[1][0] = middle_down[0] - abs(middle_down[0] - down[0]) * 0.67
        Blusher_left[2][0] = up[0]
        Blusher_left[2][1] = final[1]
        Blusher_left[3][0] = Blusher_left[1][0]
        Blusher_left[3][1] = middle_up[1] + abs(middle_up[1] - final[1]) * 0.07
        Blusher_left[1][1] = final[1] + abs(final[1] - Blusher_left[3][1])
        Blusher_left[4] = Blusher_left[0]
        if flag == 1:
            makeTxtFile(Blusher_left, "frame/squareBlusher2.txt", "a")
        else:
            makeTxtFile(Blusher_left, "frame/squareBlusher.txt", "a")
    # ----------------------------출력-------------------------------------

    xplus = True;
    d_temp_x = abs((final[0] - end_up[0]) * 2 / 3)

    if isRight:
        xplus = False;
        d_temp_x *= -1.0

    # final 2개(원) 출력
    temp_x = end_up[0] + d_temp_x
    temp_y = abs((final[1] - end_up[1]) / 2) + end_up[1]
    cv2.circle(image, (int(temp_x), int(temp_y)), 2, colors, thickness)
    temp_y = abs((final[1] - end_up[1]) / 2) + final[1]
    cv2.circle(image, (int(temp_x), int(temp_y)), 2, colors, thickness)

    # final 점 출력
    cv2.circle(image, (int(final[0]), int(final[1])), 2, colors, thickness)

    # up 과 middle_up사이
    image = draw_new(d_temp_x, xplus, True, up, middle_up, image, colors)

    # middle_up과 end_up 사이
    image = draw_new(d_temp_x, xplus, True, middle_up, end_up, image, colors)

    # down 과 middle_down 사이
    image = draw_new(d_temp_x, xplus, False, down, middle_down, image, colors)

    # middle_down 과 end_down 사이
    image = draw_new(d_temp_x, xplus, False, middle_down, end_down, image, colors)

    cv2.circle(image, (int(up[0]), int(up[1])), 2, colors, thickness)
    cv2.circle(image, (int(middle_up[0]), int(middle_up[1])), 2, colors, thickness)
    cv2.circle(image, (int(end_up[0]), int(end_up[1])), 2, colors, thickness)
    cv2.circle(image, (int(down[0]), int(down[1])), 2, colors, thickness)
    cv2.circle(image, (int(middle_down[0]), int(middle_down[1])), 2, colors, thickness)
    cv2.circle(image, (int(end_down[0]), int(end_down[1])), 2, colors, thickness)

    return image


def draw_new(num, xplus, yplus, start, end, image, color=(205, 255, 255)):
    num = abs(int((start[0] - end[0]) / (num * 1.3)))
    if num >= 1:
        dx = abs((start[0] - end[0]) / (num))
        dy = abs((start[1] - end[1]) / (num))
        if xplus == False: dx *= -1.0
        if yplus == False: dy *= -1.0
        for i in range(num):
            temp_x = start[0] + dx * (i + 1)
            temp_y = start[1] + dy * (i + 1)
            cv2.circle(image, (int(temp_x), int(temp_y)), 2, color, thickness=2)

    return image

def draw_frame_liner(dir_frame, image, colors=(20, 255, 200)):
    for i in range(len(dir_frame)):
        po = dir_frame[i]
        center = (int(po[0]), int(po[1]))
        cv2.circle(image, center, 2, colors, thickness=1)
    return image

def draw_frame(dir_frame, image, colors=(20, 255, 200)):
    for i in range(len(dir_frame)):
        po = dir_frame[i]
        center = (int(po[0]), int(po[1]))
        cv2.circle(image, center, 2, colors, thickness=2)
    return image


def makeTxtFile(npArray, txtName, mode):
    String = '\n'.join(' '.join('%d' % x for x in y) for y in npArray)
    # txt파일 생성 존재하면 수정, 존재하지 않으면 생성 후 쓰기
    f = open(txtName, mode)
    if (mode == 'a'):
        f.write("\n\n")
    f.write(String)
    f.close()
    return String

def make_lips_txt(shape):
    # 입술 배열 생성 - lipsArray.txt 파일 생성
    lips = np.zeros((14, 2), dtype="int")
    lips[0] = shape[48]
    lips[1:4] = shape[50:53]
    lips[4] = shape[54]
    lips[5] = shape[56]
    lips[6] = shape[58]
    lips[7:12] = shape[60:65]
    lips[12] = shape[65]
    lips[13] = shape[67]
    makeTxtFile(lips, "frame/lipsArray.txt", "w")


def shape_to_numpy_array(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coordinates = np.zeros((68, 2), dtype=dtype)

    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coordinates[i] = (shape.part(i).x, shape.part(i).y)

    # return the list of (x, y)-coordinates
    return coordinates

def image_to_shape(image):
    # cv2 face detector
    print("얼굴인식 시작")
    face_cascade = cv2.CascadeClassifier("face_detector/haarcascade_frontalface_default.xml")
    # dlib landmark detector
    predictor = dlib.shape_predictor("face_detector/shape_predictor_68_face_landmarks.dat")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    result = False
    if len(faces) == 1:
        rect_value = faces[0]
        rect = dlib.rectangle(int(rect_value[0]), int(rect_value[1]), int(rect_value[0] + rect_value[2]),
                          int(rect_value[1] + rect_value[3]))
        shape = predictor(gray, rect)
        shape = shape_to_numpy_array(shape)
        result = True
        return shape, result
    else:
        print("얼굴인식 실패")
        shape = 0
        return shape, result




def image_to_landmark(face):
    print("landmark start")
    # dlib에 있는 정면 얼굴검출기로 입력 사진에서 얼굴 검출하여 detected_faces로 변환
    detector = dlib.get_frontal_face_detector()
    face_pose_predictor = dlib.shape_predictor("face_detector/shape_predictor_68_face_landmarks.dat")

    detected_faces = detector(face, 0)  # detected_faces : rectangles[[(66, 137) (281, 352)]]
    pose_landmarks = face_pose_predictor(face, detected_faces[0])  # detected_face[0] : rectangle(66,137,281,352)

    landmark = np.empty([68, 2], dtype=int)
    for i in range(68):
        landmark[i][0] = pose_landmarks.part(i).x  # x값(가로)
        landmark[i][1] = pose_landmarks.part(i).y  # y값(세로)
    print("landmark end")
    return landmark

def shadowCheck():
    j = 0
    file_shadow = np.loadtxt('frame/shadowArray2.txt')
    for i in range(0, len(file_shadow)):
        print(file_shadow[i])
    if (file_shadow[9][0] >= file_shadow[4][0]):
        file_shadow[9][0] = file_shadow[9][0] - 5

    for i in range(len(file_shadow) - 18, 1, -1):
        print(len(file_shadow) - 18, 0)
        while (file_shadow[i][0] <= file_shadow[i - 1][0]):
            file_shadow[i - 1][0] -= 1

    for i in range(len(file_shadow) - 12, len(file_shadow) - 17, -1):
        print(len(file_shadow) - 12, len(file_shadow) - 17)
        while (file_shadow[i][0] <= file_shadow[i - 1][0]):
            file_shadow[i - 1][0] -= 1

    for i in range(len(file_shadow) - 7, len(file_shadow) - 11, -1):
        print(len(file_shadow) - 7, len(file_shadow) - 12)
        while (file_shadow[i][0] <= file_shadow[i - 1][0]):
            file_shadow[i - 1][0] -= 1

    for i in range(len(file_shadow) - 1, len(file_shadow) - 6, -1):
        print(len(file_shadow) - 1, len(file_shadow) - 7)
        while (file_shadow[i][0] <= file_shadow[i - 1][0]):
            file_shadow[i - 1][0] -= 1
    # print(file_shadow)
    np.savetxt('frame/shadowArray2.txt', file_shadow, fmt='%d')

def draw_draw(frame, image):
    for i in range(int(len(frame) / 2)):
        center = (int(frame[i * 2]), int(frame[i * 2 + 1]))
        cv2.circle(image, center, 2, (51, 255, 204), thickness=2)
    return image

'''
faceCapture = cv2.imread("./ex_0.png")
shape, result = image_to_shape(faceCapture)
print()

make_lips_txt(shape)

#landmark = image_to_landmark(faceCapture)
#result = Blusher("Round").frame(faceCapture, shape)
EyeBrow("Arch").frame(faceCapture, shape, True)
eye = EyeShadow("Small")
result = eye.frame(faceCapture, shape)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#립
#make_lips_txt(shape)

#블러셔  # 성공.
result = Blusher("Round").frame(faceCapture, shape)
result = Blusher("Oblong").frame(faceCapture, shape)
result = Blusher("Square").frame(faceCapture, shape)


#아이쉐도우
#result = EyeBrow("Arch").frame(faceCapture, shape, True)
# result = EyeShadow("middle").frame(image, shape)
# result = EyeShadow("Large").frame(image, shape)
# result = EyeShadow("Small").frame(image, shape)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('../ex_0.png')
image = imutils.resize(image, width=800)
shape, result = image_to_shape(image)
print("55")

result = EyeBrow("Arch").frame(image, shape, True) # eyeshadow
output = EyeShadow("middle").frame(image, shape)
print("666")
output = imutils.resize(output, width=400)
cv2.imshow('result', output)
cv2.imwrite('result_sh2.png',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

