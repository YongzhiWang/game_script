import os
import time
import cv2
from subprocess import call

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
    os.system('adb shell monkey -p com.klab.captain283.global -c android.intent.category.LAUNCHER 1')

def kill_app():
    os.system('adb shell am force-stop com.klab.captain283.global')
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
            for s in line.split(','):
                number = int(s)
                print("detect number is {}".format(number))
                break
            break
    if number < 500:
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
    if max_val > 0.99:
        print("Matched Penalty!")
        return 1
    return 0