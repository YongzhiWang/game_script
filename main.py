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
    print('USAGE: just run python main.py params.json. Put all the parameters into params.json!!!!!!!!')
    print(len(sys.argv))
    if len(sys.argv) == 2:
        param_file = sys.argv[1]
        with open(param_file) as data_file:
            parameters = json.load(data_file)
            utils.script_name = parameters["script"]
            utils.deviceID = parameters["deviceID"]
            utils.accountVersion = parameters["accountVersion"]
            utils.league_team = parameters["league_team"]
            utils.goal_keeper = parameters["goal_keeper"]
            utils.perfect_goal_keeper = parameters["perfect_goal_keeper"]
            utils.perfect_goal_keeper_stop = parameters["perfect_goal_keeper_stop"]
            utils.run_middle = parameters["run_middle"]

            if 'run_hard' in parameters:
                utils.run_hard = parameters["run_hard"]
            if 'x_offset_ratio' in parameters:
                utils.x_offset_ratio = parameters["x_offset_ratio"]
            if 'y_offset_ratio' in parameters:
                utils.y_offset_ratio = parameters["y_offset_ratio"]

            if 'x_offset' in parameters:
                utils.x_offset = parameters["x_offset"]

            if 'phone_perf' in parameters:
                utils.phone_perf = parameters["phone_perf"]

            if 'has_easy' in parameters:
                utils.has_easy = parameters["has_easy"]

            if 'sell_ssr' in parameters:
                utils.sell_ssr = parameters["sell_ssr"]



            roundCount = parameters["count"]
            for i in range(roundCount):
                print('ROUND {} begins !!!!!!!!!!!!!!!!!!!!!!!!!!'.format(i))
                a = datetime.datetime.now()
                utils.exit_current_round = 0
                actions.ScenarioExecutor(utils.script_name).execute()
                b = datetime.datetime.now()
                print('ROUND {} ENDS!!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(i))
                print('ROUND {} TAKES {} !!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(i, b-a))



