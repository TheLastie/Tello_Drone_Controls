from djitellopy import tello
from time import sleep
import pygame
import cv2
import math


class Main:
    def __init__(self):
        self.telo = tello.Tello()
        self.telo.connect()
        self.x = 0
        self.y = 0
        self.speed = 30
        self.yaw = 0

    def update(self):
        self.img = self.telo.get_frame_read().frame
        """img = cv2.imread('C:/Users/My Family/PycharmProjects/drone/123/122.jpg')"""
        img_size = 240, 120
        img1 = cv2.resize(self.img, img_size)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        a, img1 = cv2.threshold(img1, 127, 255, 0)
        self.yaw = self.img_yaw((img_size[0], img_size[1]))
        self.movement()

    def movement(self):
        if abs(self.yaw)>6:
            self.telo.send_rc_control(0, 0, 0, self.yaw)
        else:
            self.telo.send_rc_control(0, self.speed, 0, 0)










    def img_yaw(self, img_size):
        img = self.img
        points_x1 = []
        points_x2 = []
        points1_x1 = []
        points2_x2 = []
        points1 = 0
        points2 = 0
        l_start = 0
        l_starts = []

        for i in range(0, img_size[1]):
            fst = 1
            fst1 = 1
            for p in range(img_size[0]):
                if img[i, p] != img[i, p - 1]:
                    if points1 < 3 and fst1:
                        points1_x1.append(p)
                        points1 += 1
                        fst1 = 0
                    elif points2 < 3 and not fst1:
                        points2_x2.append(p)
                        points2 += 1
                    elif fst and points1 > 2:
                        points_x1.append(p)
                        fst = 0
                    elif not fst and points2 > 2:
                        points_x2.append(p)

        end_points1 = points_x1[-1], points_x1[-2], points_x1[-3]
        end_points2 = points_x2[-1], points_x2[-2], points_x2[-3]
        yaws = []
        l = 1
        for i in points_x1:
            if i:
                yaws.append(math.atan((sum(points1_x1)/3 - i) /l)/math.pi*180)
            l+=1

        return sum(yaws)/len(yaws)


if __name__ == '__main__':
    while True:
        Main().update()
