import os
import time
import cv2
import sys
from subprocess import call
import imutils
import random
import re
import codecs


def double(matched):
    matched_str = matched.group(0)
    #print("MATCHED " + matched_str[0:24])

    return matched_str[0: 24]


if __name__ == '__main__':

    whole_string = ""

    with codecs.open('input.txt', 'r', encoding='utf8') as f_input:
        with codecs.open('output.txt', 'w', encoding='utf8') as f_out:
            line = f_input.readline()
            #print("INPUT " + line)
            #print("length {}".format(len(line)))
            while line:
                if len(line) > 35 + 4:
                    correct_str = line[0:(len(line) - 6)] + "\r\n"
                    whole_string += correct_str
                else:
                    output_str = re.sub('(.{24})(@@@@)', double, line)
                    #print("OUTPUT " + output_str)
                    whole_string += output_str[:-2]
                line = f_input.readline()
                #print("INPUT " + line)
                #print("length {}".format(len(line)))



            f_out.write(re.sub('@@@@', "\r\n", whole_string))
            f_out.close()



    # FNULL = open(os.devnull, 'w')
    # crop_image_path = "./crop_league.png"
    # output_path = "./convert_text"
    #
    # call(["tesseract", crop_image_path, output_path], stdout=FNULL)
    # number = 0
    # output_file = output_path + ".txt"
    # with open(output_file, 'r') as f:
    #     for line in f:
    #         #Not sure why , is recognize as .
    #         line = line.replace(".", ",")
    #         print(line)
    #         for s in line.split(','):
    #             s = s.replace(" ", "")
    #             print s
    #             number = int(s)
    #             print("detect number is {}".format(number))
    #             break
    #         break









