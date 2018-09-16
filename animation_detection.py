import utils
import sys
import os
import cv2
from subprocess import call
import argparse
import imutils




if __name__ == '__main__':

    img = cv2.imread("screencap.png", 0)



    img2 = img.copy()
    template = cv2.imread('winning_flag.png', 0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.99:
        print("Matched!")








