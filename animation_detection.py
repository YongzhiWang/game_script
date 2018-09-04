import sys
import os
import cv2
from subprocess import call
import argparse



if __name__ == '__main__':
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    img = cv2.imread('screencap.png', 0)
    template = cv2.imread('match_middle.png', 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.95:
        print("Matched Story!")
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        #return true, (top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2



