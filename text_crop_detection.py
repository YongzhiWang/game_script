import sys
import os
import cv2
from subprocess import call
import argparse



if __name__ == '__main__':
    FNULL = open(os.devnull, 'w')
    input_image_path = "league.png"
    crop_image_path = "./league_goal_crop.png"
    output_path = "./convert_text"
    img = cv2.imread(input_image_path)
    crop_img = img[421:421+40, 563:563+120]
    cv2.imwrite(crop_image_path,crop_img)
    call(["tesseract", crop_image_path, output_path], stdout=FNULL)
    number = 0
    output_file = output_path + ".txt"
    with open(output_file, 'r') as f:
        for line in f:
            print(line)
            for s in line.split('.'):
                print(s)
                s = s.replace(" ", "")
                print(s)
                number = int(s)
                break
            break
    print(number)
