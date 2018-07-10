import sys
import actions
import datetime
import utils

def init():
    print('kill Trubasa app')
    utils.kill_app()
    utils.sleep_wait(3)
    print('launch Trubasa app')
    utils.launch_app()
    utils.sleep_wait(20)


if __name__=='__main__':
    init()
    if len(sys.argv) == 3:
            total = int(sys.argv[2])
            for i in range(total):
                print('ROUND {} begins !!!!!!!!!!!!!!!!!!!!!!!!!!'.format(i))
                a = datetime.datetime.now()
                actions.ScenarioExecutor(sys.argv[1]).execute()
                b = datetime.datetime.now()
                print('ROUND {} ENDS!!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(i))
                print('ROUND {} TAKES {} !!!!!!!!!!!!!!!!!!!!!!!!!!!.'.format(i, b-a))
    else:
        print("Usage: python main.py data.json 10")

