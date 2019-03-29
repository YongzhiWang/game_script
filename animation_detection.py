import os
import time
import cv2
import sys
from subprocess import call
import imutils
import random
import re
import codecs
import sys
import cv2
import actions
import datetime
import utils
import json
import urllib
import urllib2
import locale


def double(matched):
    matched_str = matched.group(0)
    #print("MATCHED " + matched_str[0:24])

    return matched_str[0: 24]

def sortSecond(val):

    return val["price"]


if __name__ == '__main__':
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
    new_dict = []
    playerNames = {}

    with open("players.json") as player_file:
        playerNamesObj = json.load(player_file)
        normalPlayerObj = playerNamesObj["Players"]
        for player_name in normalPlayerObj:
            playerNames[player_name["id"]] = player_name["f"] + " " + player_name["l"]


    with open("memberlist_1.json") as data_file:
        allplayer = json.load(data_file)
        allPlayerDataList = allplayer["itemData"]
        count = 1
        for player in allPlayerDataList:
            if player["untradeable"] == 0 and player["rating"] <= 85 and player["rating"] >= 75:
                print("user id {}".format(player["resourceId"]))
                print("user rating {}".format(player["rating"]))
                print("user preferredPosition {}".format(player["preferredPosition"]))
                url = "https://www.futbin.com/19/playerPrices?player={}".format(player["resourceId"])
                print url
                req = urllib2.Request(url)
                req.add_header('authority', 'www.futbin.com')
                req.add_header('pragma', 'no-cache')
                req.add_header('upgrade-insecure-requests', '1')
                req.add_header('cache-control', 'no-cache')
                req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
                req.add_header('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
                #req.add_header('accept-encoding', 'gzip, deflate, br')
                req.add_header('accept-language', 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7')
                req.add_header('cookie', '__cfduid=dd7d180f7558cf79415f75da18160b1cb1548053912; _ga=GA1.2.475080697.1548053928; __gads=ID=8d22e159b5643750:T=1548053930:S=ALNI_Man-OODx-ARclJ2c7MnB4fFq8l00g; PHPSESSID=ec5ecf9b24c90d7bfdab87208a401520; comments=true; platform=ps4; _gid=GA1.2.489940667.1548927690; xbox=true; ps=true; pc=true; sc_is_visitor_unique=rx9767571.1548933216.1228D1DBA8814F73C659BA780EABA8A9.6.6.5.4.4.4.4.4.2')

                res_data = urllib2.urlopen(req)

                playerData = json.load(res_data)
                count = count + 1

                ave_price = (locale.atoi(playerData["{}".format(player["resourceId"])]["prices"]["ps"]["LCPrice"]) + locale.atoi(playerData["{}".format(player["resourceId"])]["prices"]["ps"]["LCPrice2"]) + locale.atoi(playerData["{}".format(player["resourceId"])]["prices"]["ps"]["LCPrice3"]) + locale.atoi(playerData["{}".format(player["resourceId"])]["prices"]["ps"]["LCPrice4"])) / 4


                print "Count : {}".format(count)
                #print "Player name : {}".format(playerNames[player["resourceId"]])

                #print playerData["{}".format(player["resourceId"])]
                if player["resourceId"] in playerNames:
                    playerDataObj = {
                        "ID":player["resourceId"],
                        "rating" : player["rating"],
                        "position" : player["preferredPosition"],
                        "price" : ave_price,
                        "name" : playerNames[player["resourceId"]]
                    }
                    new_dict.append(
                        playerDataObj
                    )
                else:
                    playerDataObj = {
                        "ID":player["resourceId"],
                        "rating" : player["rating"],
                        "position" : player["preferredPosition"],
                        "price" : ave_price
                    }
                    new_dict.append(
                        playerDataObj
                    )





                new_dict.sort(key=sortSecond, reverse = True)

                print new_dict

                #print playerData["{}".format(player["resourceId"])]["prices"]["ps"]["LCPrice"]

                #print res
                time.sleep(5)

    new_dict.sort(key = sortSecond, reverse = True)

    print new_dict
    #print



#         self.senario = json.load(data_file)
#
# def execute(self):
#     for action in self.senario:
#         if utils.exit_current_round == 0:
#
#         utils.script_name = parameters["script"]
#         utils.deviceID = parameters["deviceID"]
#         utils.accountVersion = parameters["accountVersion"]
#         utils.league_team = parameters["league_team"]
#         utils.goal_keeper = parameters["goal_keeper"]
#         utils.perfect_goal_keeper = parameters["perfect_goal_keeper"]
#         utils.perfect_goal_keeper_stop = parameters["perfect_goal_keeper_stop"]
#         utils.run_middle = parameters["run_middle"]
#
#     whole_string = ""
#
#     with codecs.open('input.txt', 'r', encoding='utf8') as f_input:
#         with codecs.open('output.txt', 'w', encoding='utf8') as f_out:
#             line = f_input.readline()
#             #print("INPUT " + line)
#             #print("length {}".format(len(line)))
#             while line:
#                 if len(line) > 35 + 4:
#                     correct_str = line[0:(len(line) - 6)] + "\r\n"
#                     whole_string += correct_str
#                 else:
#                     output_str = re.sub('(.{24})(@@@@)', double, line)
#                     #print("OUTPUT " + output_str)
#                     whole_string += output_str[:-2]
#                 line = f_input.readline()
#                 #print("INPUT " + line)
#                 #print("length {}".format(len(line)))
#
#
#
#             f_out.write(re.sub('@@@@', "\r\n", whole_string))
#             f_out.close()



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









