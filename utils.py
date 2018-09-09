import os
import time
import cv2
import sys
from subprocess import call

script_name = ""
deviceID = ""
accountVersion = 1
league_team = 270
goal_keeper = 7
perfect_goal_keeper = 10
perfect_goal_keeper_stop = 0
run_middle = 0
run_hard = 0
use_energy_ball = 0

def tap_screen(x, y):
    os.system('adb -s {} shell input tap {} {}'.format(deviceID, x,y))

def sleep_wait(total_time):
   for i in range(total_time):
        print('sleep {} second.'.format(i))
        time.sleep(1)
        # keep the device on
        os.system('adb -s {} shell input keyevent 82'.format(deviceID))

def sleep_wait_detect(total_time, detect_times):
    for i in range(total_time):
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
    if accountVersion == 1:
        os.system('adb -s {} shell monkey -p com.klab.captain283.global -c android.intent.category.LAUNCHER 1'.format(deviceID))
    elif accountVersion == 2:
        os.system('adb -s {} shell monkey -p com.klab.captain283.globan -c android.intent.category.LAUNCHER 1'.format(deviceID))
    elif accountVersion == 3:
        os.system('adb -s {} shell monkey -p com.klab.captain283.globao -c android.intent.category.LAUNCHER 1'.format(deviceID))


def kill_app():
    if accountVersion == 1:
        os.system('adb -s {} shell am force-stop com.klab.captain283.global'.format(deviceID))
    elif accountVersion == 2:
        os.system('adb -s {} shell am force-stop com.klab.captain283.globan'.format(deviceID))
    elif accountVersion == 3:
        os.system('adb -s {} shell am force-stop com.klab.captain283.globao'.format(deviceID))

    kill_all()

def kill_all():
    os.system('adb -s {} shell am kill-all'.format(deviceID))

def horizontal_swipe_screen():
    for i in range(0, 4):
        os.system('adb -s {} shell input swipe 1800 500 0 500'.format(deviceID))
        time.sleep(0.2)

def horizontal_swipe_screen_once():
    os.system('adb -s {} shell input swipe 900 500 0 500'.format(deviceID))
    time.sleep(0.2)

def vertical_swipe_screen_up():
    for i in range(0,3):
        os.system('adb -s {} shell input swipe 1400 800 1400 100'.format(deviceID))
        time.sleep(0.2)

def vertical_swipe_screen_down():
    os.system('adb -s {} shell input swipe 1400 100 1400 300'.format(deviceID))
    time.sleep(0.2)

def isValidLeagueUser():
    screencap_file = pull_screenshot()
    FNULL = open(os.devnull, 'w')
    input_image_path = screencap_file
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
    template = cv2.imread(target_pattern_file, 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("Detect {} result {}!".format(target_pattern_file, max_val))
    if max_val > 0.95:
        print("Matched {}!".format(target_pattern_file))
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        return 1, (top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2
    return 0, 0, 0

def hasEnergyBall():
    screencap_file = pull_screenshot()
    img = cv2.imread(screencap_file, 0)
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