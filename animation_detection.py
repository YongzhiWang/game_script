import sys
import os
import cv2
from subprocess import call
import argparse



if __name__ == '__main__':
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    img = cv2.imread('screencap.png', 0)
    crop_img = img[0:340, 0:1920]

    crop_image_path = "./crop_story.png"
    cv2.imwrite(crop_image_path,crop_img)

    template = cv2.imread('unread_story.png', 0)
    img = crop_img.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.99:
        print("Matched Story!")

