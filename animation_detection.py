import utils
import sys
import os
import cv2
from subprocess import call
import argparse
import imutils




if __name__ == '__main__':
    utils.deviceID = "192.168.93.69:5556"
    x_offset_ratio = 1.33
    y_offset_ratio = 1.33

    print(1 / x_offset_ratio)
    img = cv2.imread("screencap192.168.92.243:5555.png", 0)
    if x_offset_ratio >1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440/1.33))
        cv2.imshow("Width=%dpx", img)

        #crop_image_path = "./crop_league.png"
        #cv2.imwrite(crop_image_path,img)


    img2 = img.copy()
    template = cv2.imread('someone_join_pattern.png', 0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.99:
        print("Matched!")








