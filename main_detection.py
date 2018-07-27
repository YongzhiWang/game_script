import cv2
import os
import datetime

if __name__ == '__main__':
    a = datetime.datetime.now()
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    b = datetime.datetime.now()
    print('Take screenshot TAKES {} !!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(b-a))
    img = cv2.imread('screencap.png', 0)
    img2 = img.copy()
    template = cv2.imread('winning_flag.png', 0)
    w, h = template.shape[::-1]

    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')

    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print("matching result:")
    print(min_val)
    print(max_val)
    print(top_left)
    print(bottom_right)
    if max_val > 0.99:
        print("Matched!")

    b = datetime.datetime.now()
    print('TOTAL TAKES {} !!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(b-a))

