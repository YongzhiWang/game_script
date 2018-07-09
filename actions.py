import utils
import json

class BaseActionInfo:
    globalDelay = 0

    def __init__(self, message, actionDelay):
        self.message = message
        self.actionDelay = actionDelay

    def execute(self):
        print(self.message)
        if self.actionDelay > 0:
            utils.sleep_wait(self.actionDelay + self.globalDelay)

class TapActionInfo(BaseActionInfo):

    def __init__(self, xpos, ypos, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.xpos = xpos
        self.ypos = ypos

    def execute(self):
        utils.tap_screen(self.xpos, self.ypos)
        BaseActionInfo.execute(self)

class SleepActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, 0)
        self.sleepTime = sleepTime

    def execute(self):
        BaseActionInfo.execute(self)
        utils.sleep_wait(self.sleepTime)

class KillActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self, message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        utils.kill_app()
        BaseActionInfo.execute(self)

class LaunchActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        utils.launch_app()
        BaseActionInfo.execute(self)

class SwipeEndActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        utils.horizontal_swipe_screen()
        BaseActionInfo.execute(self)


class ActionExecutor:

    def __init__(self, jsonObject):
        self.jsonObject = jsonObject


    def executeJson(self):
        #print json.dumps(self.jsonObject, indent=4, sort_keys=True)
        actionName = self.jsonObject["action"]
        if actionName == "kill":
            KillActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "launch":
            LaunchActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "swipe_end":
            SwipeEndActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "tap":
            TapActionInfo(self.jsonObject["xpos"], self.jsonObject["ypos"], self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "sleep":
            SleepActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()


class ScenarioExecutor:

    def __init__(self, filePath):
        with open(filePath) as data_file:
            self.senario = json.load(data_file)

    def execute(self):
        for action in self.senario:
            singleAction = ActionExecutor(action)
            singleAction.executeJson()