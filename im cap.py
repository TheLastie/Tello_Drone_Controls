from djitellopy import tello
import cv2


def img_vector(img, img_size):
    points_x1 = []
    points_x2 = []
    points1_x1 = []
    points2_x2 = []
    points1 = 0
    points2 = 0

    for i in range(img_size[1]):
        fst = 1
        fst1 = 1
        for p in range(img_size[0]):
            if img[i, p] != img[i, p - 1]:
                if points1 < 4 and fst1:
                    points1_x1.append(p)
                    points1 += 1
                    fst1 = 0
                elif points2 < 4 and not fst1:
                    points2_x2.append(p)
                    points2 += 1
                elif fst and points1 > 3:
                    points_x1.append(p)
                    fst = 0
                elif not fst and points2 > 3:
                    points_x2.append(p)

    print(sum(points1_x1), len(points1_x1), sum(points_x1), len(points_x1))
    print(sum(points2_x2), len(points2_x2), sum(points_x2), len(points_x2))

    mid_points1 = abs((sum(points1_x1) + sum(points_x1) // (len(points1_x1) + len(points_x1))))
    mid_points2 = abs((sum(points2_x2) + (sum(points_x2)) // (len(points_x2)+len(points2_x2))))
    mid_point_x = (mid_points1 + mid_points2) / 2
    vector = mid_point_x, (len(points_x1) + len(points_x2) - len(points1_x1) - len(points2_x2)) / 2
    print(points1_x1, points2_x2, points_x1, points_x2)
    return vector


'''me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

img = cv2.imread('C:/Users/My Family/PycharmProjects/drone/123/')
img = cv2.resize(img, (360, 240))
cv2.imshow("Image", img)
cv2.waitKey(1)
'''

"""img = self.telo.get_frame_read().frame"""
img = cv2.imread('C:/Users/My Family/PycharmProjects/drone/123/1233.jpg')
img1 = cv2.resize(img, (240, 120))
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
o = 0
for i in range(0, 240-1):
    for p in range(0, 120-1):
        o += img1[p, i]
o = o // (240*120)
a, img1 = cv2.threshold(img1,  130, 255, 0)
print(img_vector(img1, (240, 120)))

cv2.imshow("Image", img1)
cv2.waitKey(1000)

