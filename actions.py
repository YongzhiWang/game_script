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

class SleepAndDetectActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime, detectTimes):
        BaseActionInfo.__init__(self,message, 0)
        self.sleepTime = sleepTime
        self.detectTimes = detectTimes

    def execute(self):
        BaseActionInfo.execute(self)
        utils.sleep_wait_detect(self.sleepTime, self.detectTimes)

class SleepAndDetectCoachActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime, detectTimes):
        BaseActionInfo.__init__(self,message, 0)
        self.sleepTime = sleepTime
        self.detectTimes = detectTimes

    def execute(self):
        BaseActionInfo.execute(self)
        result = utils.sleep_wait_detect(self.sleepTime, self.detectTimes)
        if result > 0:
            ScenarioExecutor("s6_training_coach_job.json").execute()

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

class SwipeOnceActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        utils.horizontal_swipe_screen_once()
        BaseActionInfo.execute(self)

class SwipeToBottomActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        utils.vertical_swipe_screen_up()
        BaseActionInfo.execute(self)

class LeagueActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime, count):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.message = message
        self.sleepTime = sleepTime
        self.count = count

    def execute(self):
        for i in range(self.count):
            result = utils.isValidLeagueUser()
            if result > 0:
                ScenarioExecutor("s6_go_into_league.json").execute()
                goalkeeper = utils.isValidLeagueGoalKeeper()
                if goalkeeper > 0:
                    ScenarioExecutor("s6_go_back_league_inner.json").execute()
                    ScenarioExecutor("s6_begin_league_match.json").execute()
                    return
                # goback to leage.
                ScenarioExecutor("s6_go_back_league_inner.json").execute()
            ScenarioExecutor("s6_go_back_league.json").execute()

        ScenarioExecutor("s6_go_back_home.json").execute()
        BaseActionInfo.execute(self)

class LeagueDetectActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime, count):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.message = message
        self.sleepTime = sleepTime
        self.count = count

    def execute(self):
        for i in range(self.count):
            result = utils.isValidLeagueUser()
            if result > 0:
                ScenarioExecutor("s6_go_into_league.json").execute()
                goalkeeper = utils.isValidLeagueGoalKeeper()
                if goalkeeper > 0:
                    return
                # goback to leage.
                ScenarioExecutor("s6_go_back_league_inner.json").execute()
            ScenarioExecutor("s6_go_back_league.json").execute()

        ScenarioExecutor("s6_go_back_home.json").execute()
        BaseActionInfo.execute(self)

class PenaltyActionInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        result = utils.isRunningPenatly()
        if result > 0:
            # Just handle the 8v8 cases without fancy for loop.
            ScenarioExecutor("s6_do_penalty.json").execute()

        #    "xpos": 1265,
        #    "xpos": 1515
        #    "xpos": 1765

        BaseActionInfo.execute(self)

class CheckAnimationInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        result = utils.isUnreadStory()
        if result > 0:
            # Just handle the 8v8 cases without fancy for loop.
            ScenarioExecutor("s6_auto_self_animation.json").execute()
        else:
            ScenarioExecutor("s6_auto_self_juqing.json").execute()
        BaseActionInfo.execute(self)

class CheckMatchInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        for i in range(0, 2):
            easymatch, xpox, ypos = utils.hasEasyMatch()
            if easymatch > 0:
                utils.tap_screen(xpox, ypos)
                ScenarioExecutor("s6_partial_match.json").execute()
                return
            else:
                middleMatch, xpox, ypos = utils.hasMiddleMatch()
                if middleMatch > 0:
                    utils.tap_screen(xpox, ypos)
                    ScenarioExecutor("s6_partial_match.json").execute()
                    return
                #dd
            # not found
            utils.vertical_swipe_screen_down()

        BaseActionInfo.execute(self)

class ActionExecutor:

    def __init__(self, jsonObject):
        self.jsonObject = jsonObject


    def executeJson(self):
        #print "inner"
        #print json.dumps(self.jsonObject, indent=4, sort_keys=True)
        actionName = self.jsonObject["action"]
        if actionName == "kill":
            KillActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "launch":
            LaunchActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "swipe_end":
            SwipeEndActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "swipe_bottom":
            SwipeToBottomActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "tap":
            TapActionInfo(self.jsonObject["xpos"], self.jsonObject["ypos"], self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "sleep":
            SleepActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "sleep_detect":
            SleepAndDetectActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"], self.jsonObject["detectTimes"]).execute()
        elif actionName == "sleep_detect_coach":
            SleepAndDetectCoachActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"], self.jsonObject["detectTimes"]).execute()
        elif actionName == "swipe":
            SwipeOnceActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "league":
            LeagueActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"], self.jsonObject["count"]).execute()
        elif actionName == "league_detect":
            LeagueDetectActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"], self.jsonObject["count"]).execute()
        elif actionName == "do_penalty":
            PenaltyActionInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "check_animation":
            CheckAnimationInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "check_match":
            CheckMatchInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "script":
            print "enter script"
            ScenarioExecutor(self.jsonObject["fileName"]).execute()


class ScenarioExecutor:

    def __init__(self, filePath):
        #print filePath
        with open(filePath) as data_file:
            self.senario = json.load(data_file)

    def execute(self):
        for action in self.senario:
            #print json.dumps(action, indent=4, sort_keys=True)
            singleAction = ActionExecutor(action)
            singleAction.executeJson()