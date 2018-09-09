import sys
import cv2
import actions
import datetime
import utils
import json

def init():
    print('kill Trubasa app')
    #utils.kill_app()
    #utils.sleep_wait(3)
    print('launch Trubasa app')
    #utils.launch_app()
    #utils.sleep_wait(20)


if __name__=='__main__':
    init()
    with open("auto_match_script_parameters.json") as data_file:
        parameters = json.load(data_file)
        utils.script_name = parameters["script"]
        utils.deviceID = parameters["deviceID"]
        utils.accountVersion = parameters["accountVersion"]
        utils.league_team = parameters["league_team"]
        utils.goal_keeper = parameters["goal_keeper"]
        utils.perfect_goal_keeper = parameters["perfect_goal_keeper"]
        utils.perfect_goal_keeper_stop = parameters["perfect_goal_keeper_stop"]
        roundCount = parameters["count"]
        for i in range(roundCount):
            print('ROUND {} begins !!!!!!!!!!!!!!!!!!!!!!!!!!'.format(i))
            a = datetime.datetime.now()
            actions.ScenarioExecutor(utils.script_name).execute()
            b = datetime.datetime.now()
            print('ROUND {} ENDS!!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(i))
            print('ROUND {} TAKES {} !!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(i, b-a))


