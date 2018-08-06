import sys
import os
import cv2
from subprocess import call
import argparse

FNULL = open(os.devnull, 'w')

if __name__ == '__main__':
    input_image_path = "league.png"
    crop_image_path = "./crop_league.png"
    output_path = "./convert_text.txt"
    img = cv2.imread(input_image_path)
    crop_img = img[640:640+57, 1290:1290+233]
    cv2.imwrite(crop_image_path,crop_img)
    call(["tesseract", crop_image_path, output_path], stdout=FNULL)
    number = 0
    with open(output_path, 'r') as f:
        for line in f:
            for s in line.split(','):
                number = int(s)
                break
            break
    print(number)
