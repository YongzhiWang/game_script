import os
import time
import cv2
import sys
from subprocess import call

appVersion = 1

def tap_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x,y))

def sleep_wait(total_time):
   for i in range(total_time):
        print('sleep {} second.'.format(i))
        time.sleep(1)
        # keep the device on
        os.system('adb shell input keyevent 82')

def sleep_wait_detect(total_time, detect_times):
    for i in range(total_time):
        print('sleep {} second.'.format(i))
        time.sleep(1)
        # keep the device on
        os.system('adb shell input keyevent 82')

    for j in range(detect_times):
        print("Detect rounds {}!".format(j))
        result = image_detection()
        if result > 0:
            return 1
    return 0

def image_detection():
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    img = cv2.imread('screencap.png', 0)
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
        return 1
    return 0

def launch_app():
    if appVersion == 1:
        os.system('adb shell monkey -p com.klab.captain283.global -c android.intent.category.LAUNCHER 1')
    elif appVersion == 2:
        os.system('adb shell monkey -p com.klab.captain283.globan -c android.intent.category.LAUNCHER 1')
    elif appVersion == 3:
        os.system('adb shell monkey -p com.klab.captain283.globao -c android.intent.category.LAUNCHER 1')


def kill_app():
    if appVersion == 1:
        os.system('adb shell am force-stop com.klab.captain283.global')
    elif appVersion == 2:
        os.system('adb shell am force-stop com.klab.captain283.globan')
    elif appVersion == 3:
        os.system('adb shell am force-stop com.klab.captain283.globao')

    kill_all()

def kill_all():
    os.system('adb shell am kill-all')

def horizontal_swipe_screen():
    os.system('adb shell input swipe 1800 500 0 500')
    time.sleep(0.2)
    os.system('adb shell input swipe 1800 500 0 500')
    time.sleep(0.2)
    os.system('adb shell input swipe 1800 500 0 500')
    time.sleep(0.2)
    os.system('adb shell input swipe 1800 500 0 500')
    time.sleep(0.2)
    os.system('adb shell input swipe 1800 500 0 500')
    time.sleep(0.2)

def horizontal_swipe_screen_once():
    os.system('adb shell input swipe 900 500 0 500')
    time.sleep(0.2)

def vertical_swipe_screen_up():
    os.system('adb shell input swipe 1400 800 1400 100')
    time.sleep(0.2)
    os.system('adb shell input swipe 1400 800 1400 100')
    time.sleep(0.2)
    os.system('adb shell input swipe 1400 800 1400 100')
    time.sleep(0.2)

def vertical_swipe_screen_down():
    os.system('adb shell input swipe 1400 100 1400 300')
    time.sleep(0.2)

def isValidLeagueUser():
    os.system('adb shell screencap -p /sdcard/league.png')
    os.system('adb pull /sdcard/league.png')
    FNULL = open(os.devnull, 'w')
    input_image_path = "league.png"
    crop_image_path = "./crop_league.png"
    output_path = "./convert_text"
    img = cv2.imread(input_image_path)
    crop_img = img[640:640+57, 1290:1290+233]
    cv2.imwrite(crop_image_path,crop_img)
    call(["tesseract", crop_image_path, output_path], stdout=FNULL)
    number = 0
    output_file = output_path + ".txt"
    with open(output_file, 'r') as f:
        for line in f:
            line = line.replace(".", ",")
            print(line)
            for s in line.split(','):
                s = s.replace(" ", "")
                print(s)
                number = int(s)
                print("detect number is {}".format(number))
                break
            break
    if number < 300:
        return 1
    return 0

def isUnreadStory():
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    img = cv2.imread('screencap.png', 0)
    crop_img = img[0:340, 0:1920]
    template = cv2.imread('unread_story.png', 0)
    img = crop_img.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.90:
        print("Matched Story!")
        return 1
    return 0

def isRunningPenatly():
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    img = cv2.imread('screencap.png', 0)
    img2 = img.copy()
    template = cv2.imread('penalty_flag.png', 0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.90:
        print("Matched Penalty!")
        return 1
    return 0

def isValidLeagueGoalKeeper():
    os.system('adb shell screencap -p /sdcard/league.png')
    os.system('adb pull /sdcard/league.png')
    FNULL = open(os.devnull, 'w')
    input_image_path = "league.png"
    crop_image_path = "./crop_league.png"
    output_path = "./convert_text"
    img = cv2.imread(input_image_path)
    crop_img = img[421:421+40, 563:563+120]
    cv2.imwrite(crop_image_path,crop_img)
    call(["tesseract", crop_image_path, output_path], stdout=FNULL)
    number = 0
    output_file = output_path + ".txt"
    with open(output_file, 'r') as f:
        for line in f:
            #Not sure why , is recognize as .
            line = line.replace(".", ",")
            print(line)
            for s in line.split(','):
                s = s.replace(" ", "")
                print s
                number = int(s)
                print("detect number is {}".format(number))
                break
            break
    if number < 10:
        print("Ruoji goal keeper!!!!!")
        #sys.exit(0)
    if number < 16:
        return 1
    return 0

def hasEasyMatch():
    os.system('adb shell screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png')
    img = cv2.imread('screencap.png', 0)
    template = cv2.imread('match_easy.png', 0)
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
        return 1, (top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2
    return 0, 0, 0

def hasMiddleMatch():
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
        return 1, (top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2
    return 0, 0, 0
