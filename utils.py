import os
import time
import cv2
import sys
from subprocess import call
import imutils
import random
import numpy as np

script_name = ""
deviceID = ""
accountVersion = 1
league_team = 560
goal_keeper = 11
perfect_goal_keeper = 10
perfect_goal_keeper_stop = 0
run_middle = 0
run_hard = 0
use_energy_ball = 0
x_offset_ratio = 1
y_offset_ratio = 1
x_offset = 0
phone_perf = 1
has_easy = 0
sell_ssr = 0
exit_current_round = 0


def accurate_tap_screen(x, y):
    targetX = x * x_offset_ratio
    targetY = y *y_offset_ratio
    targetX = targetX
    targetY = targetY

    print('adb -s {} shell input tap {} {}'.format(deviceID, targetX, targetY))
    os.system('adb -s {} shell input tap {} {}'.format(deviceID, targetX, targetY))


def tap_screen(x, y):
    targetX = x * x_offset_ratio + x_offset
    targetY = y *y_offset_ratio
    targetX = targetX
    targetY = targetY

    print('adb -s {} shell input tap {} {}'.format(deviceID, targetX, targetY))
    os.system('adb -s {} shell input tap {} {}'.format(deviceID, targetX, targetY))

def pure_sleep(total_time):
    time.sleep(total_time)

def sleep_wait(total_time):
   for i in range((int)(total_time * phone_perf)):
        print('sleep {} second.'.format(i))
        time.sleep(1)
        # keep the device on
        os.system('adb -s {} shell input keyevent 82'.format(deviceID))

def sleep_wait_detect(total_time, detect_times):
    for i in range((int)(total_time * phone_perf)):
        print('sleep {} second.'.format(i))
        time.sleep(1)
        # keep the device on
        os.system('adb -s {} shell input keyevent 82'.format(deviceID))

    for j in range(detect_times):
        print("Detect rounds {}!".format(j))
        result = image_detection()
        if result > 0:
            return 1
    return 0

def pull_screenshot():
    os.system('adb -s {} shell screencap -p /sdcard/screencap{}.png'.format(deviceID, deviceID))
    os.system('adb -s {} pull  /sdcard/screencap{}.png'.format(deviceID, deviceID))
    return 'screencap{}.png'.format(deviceID)

def image_detection():
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)

    if x_offset_ratio > 1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    img2 = img.copy()
    template = cv2.imread('winning_flag.png', 0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect result {}!".format(max_val))
    if max_val > 0.95:
        print("Matched!")
        return 1
    return 0

def sleep_detect_pattern(presleepSeconds, detect_times, pattern):
    sleep_wait(presleepSeconds)

    for j in range(detect_times):
        print("Detect rounds {} pattern: {}!".format(j, pattern))
        result, centerX, centerY = patternDetect(pattern)
        if result > 0:
            print("Matched pattern !")
            return result, centerX, centerY

    return 0, 0, 0

def sleep_detect_scroll_pattern(presleepSeconds, detect_times, pattern):
    sleep_wait(presleepSeconds)

    for j in range(detect_times):
        print("Detect rounds {} pattern: {}!".format(j, pattern))
        result, centerX, centerY = patternDetect(pattern)
        if result > 0:
            print("Matched pattern !")
            return result, centerX, centerY
        horizontal_swipe_screen_once()

    return 0, 0, 0


def launch_app():
    if accountVersion == 1:
        os.system('adb -s {} shell monkey -p com.klab.captain283.global -c android.intent.category.LAUNCHER 1'.format(deviceID))
    elif accountVersion == 2:
        os.system('adb -s {} shell monkey -p com.klab.captain283.globan -c android.intent.category.LAUNCHER 1'.format(deviceID))
    elif accountVersion == 3:
        os.system('adb -s {} shell monkey -p com.klab.captain283.globao -c android.intent.category.LAUNCHER 1'.format(deviceID))
    elif accountVersion == 4:
        os.system('adb -s {} shell monkey -p com.klab.captain283.globam -c android.intent.category.LAUNCHER 1'.format(deviceID))


def kill_app():
    if accountVersion == 1:
        os.system('adb -s {} shell am force-stop com.klab.captain283.global'.format(deviceID))
    elif accountVersion == 2:
        os.system('adb -s {} shell am force-stop com.klab.captain283.globan'.format(deviceID))
    elif accountVersion == 3:
        os.system('adb -s {} shell am force-stop com.klab.captain283.globao'.format(deviceID))
    elif accountVersion == 4:
        os.system('adb -s {} shell am force-stop com.klab.captain283.globam'.format(deviceID))

    kill_all()

def kill_all():
    os.system('adb -s {} shell am kill-all'.format(deviceID))

def horizontal_swipe_screen_back():
    for i in range(0, 4):
        os.system('adb -s {} shell input swipe 0 500 1800 500'.format(deviceID))
        time.sleep(0.2)

def horizontal_swipe_screen():
    for i in range(0, 4):
        os.system('adb -s {} shell input swipe 1300 500 0 500'.format(deviceID))
        time.sleep(0.2)

def horizontal_swipe_screen_once():
    os.system('adb -s {} shell input swipe 900 500 0 500'.format(deviceID))
    time.sleep(1)

def vertical_swipe_screen_up():
    for i in range(0,3):
        os.system('adb -s {} shell input swipe 1400 800 1400 100'.format(deviceID))
        time.sleep(0.2)

def vertical_swipe_screen_down():
    os.system('adb -s {} shell input swipe 1400 100 1400 300'.format(deviceID))
    time.sleep(1)

def isValidLeagueUser():
    screencap_file = pull_screenshot()
    FNULL = open(os.devnull, 'w')
    input_image_path = screencap_file
    crop_image_path = "./crop_league.png"
    output_path = "./convert_text"

    img = cv2.imread(screencap_file, 0)

    if x_offset_ratio > 1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    #img = cv2.imread(input_image_path)
    crop_img = img[640:640+57, (int)(1290 + x_offset): (int)(1290+233 + x_offset)]
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
    if number < league_team:
        return 1
    return 0

def isUnreadStory():
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)
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
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)
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
    screencap_file = pull_screenshot()
    FNULL = open(os.devnull, 'w')
    input_image_path = screencap_file
    crop_image_path = "./crop_league.png"
    output_path = "./convert_text"
    img = cv2.imread(input_image_path)

    #if x_offset_ratio > 1 and y_offset_ratio > 1:
    #    print("Need to resize")
    #    img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    crop_img = img[(int)(421 * y_offset_ratio): (int)((421+40) * y_offset_ratio), (int) ((x_offset + 563) * x_offset_ratio): (int)((563+120+ x_offset)*x_offset_ratio)]
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
    if number < perfect_goal_keeper:
        print("Ruoji goal keeper!!!!!")
        if perfect_goal_keeper_stop > 0:
            sys.exit(0)
    if number < goal_keeper:
        return 1
    return 0

def hasEnergyAds():
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)

    if x_offset_ratio > 1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    template = cv2.imread('energy_watch_ads_patten.png', 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect hasEnergyAds result {}!".format(max_val))
    if max_val > 0.95:
        print("Matched hasEnergyAds!")
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        return 1
    return 0

def patternDetect(target_pattern_file):
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)
    if x_offset_ratio > 1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    template = cv2.imread(target_pattern_file, 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)

    threshold = 0.945
    loc = np.where( res >= threshold)
    xpos = []
    ypos = []
    for pt in zip(*loc[::-1]):
        #cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print("Matched {} x: {} y:{}!".format(target_pattern_file, pt[0] + w /2, pt[1] + h /2))
        xpos.append(pt[0] + w /2)
        ypos.append(pt[1] + h /2)

        #cv2.rectangle(img, pt, (pt[0] + w /2, pt[1] + h /2), (0,255,255), 2)
    #cv2.imwrite('res.png',img)

    if len(xpos) >= 1:
        print("Total matched {}!".format(len(xpos)))
        position = random.randint(1,len(xpos)) - 1
        print("Random matched {}!".format(position))

        return 1, xpos[position], ypos[position]

    return 0, 0, 0

def hasEnergyBall():
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)

    if x_offset_ratio > 1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    template = cv2.imread('energy_ball_pattern.png', 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect hasEnergyBall result {}!".format(max_val))
    if max_val > 0.95:
        print("Matched hasEnergyBall!")
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        return 1
    return 0

def hasTooManyWarning():
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)

    if x_offset_ratio > 1 and y_offset_ratio > 1:
        print("Need to resize")
        img = imutils.resize(img, height=(int)(1440 / x_offset_ratio))

    template = cv2.imread('too_many_pattern.png', 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect hasTooManyWarning result {}!".format(max_val))
    if max_val > 0.95:
        print("Matched hasTooManyWarning!")
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        return 1
    return 0