import os
import time

def tap_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x,y))

def sleep_wait(total_time):
   for i in range(total_time):
        print('sleep {} second.'.format(i))
        time.sleep(1)
        # keep the device on
        os.system('adb shell input keyevent 82')

def launch_app():
    os.system('adb shell monkey -p com.klab.captain283.global -c android.intent.category.LAUNCHER 1')

def kill_app():
    os.system('adb shell am force-stop com.klab.captain283.global')

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
