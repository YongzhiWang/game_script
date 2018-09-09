import utils
import json
import sys

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
        for i in range(0, 10):
            easymatch, xpox, ypos = utils.patternDetect("match_easy.png")
            print("Easy match result {}  {}   {}!".format(easymatch, xpox, ypos))
            if easymatch > 0:
                utils.tap_screen(xpox, ypos)
                utils.sleep_wait(1)
                ScenarioExecutor("s6_partial_match.json").execute()
                return
            elif utils.run_middle > 0:
                middleMatch, xpox, ypos =  utils.patternDetect("match_middle.png")
                print("Middle match result {}  {}   {}!".format(middleMatch, xpox, ypos))
                if middleMatch > 0:
                    utils.tap_screen(xpox, ypos)
                    utils.sleep_wait(1)
                    ScenarioExecutor("s6_partial_match.json").execute()
                    return
                elif utils.run_hard > 0:
                    hard_match, xpox, ypos =  utils.patternDetect("match_hard.png")
                    print("Hard match result {}  {}   {}!".format(hard_match, xpox, ypos))
                    if hard_match > 0:
                        utils.tap_screen(xpox, ypos)
                        utils.sleep_wait(1)
                        ScenarioExecutor("s6_partial_match.json").execute()
                        return
                #dd
            # not found
            utils.vertical_swipe_screen_down()

        BaseActionInfo.execute(self)

class CheckCategoryInfo(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        for i in range(0, 10):
            middle_match, xpox, ypos = utils.patternDetect("only_easy_done_pattern.png")
            print("Find middle match result {}  {}   {}!".format(middle_match, xpox, ypos))
            if middle_match > 0:
                utils.tap_screen(xpox, ypos)
                utils.sleep_wait(1)
                return
            elif utils.run_hard > 0:
                hard_match, xpox, ypos = utils.patternDetect("only_hard_left_pattern.png")
                print("Find hard match result {}  {}   {}!".format(hard_match, xpox, ypos))
                if hard_match > 0:
                    utils.tap_screen(xpox, ypos)
                    utils.sleep_wait(1)
                    return
                #dd
            # not found
            utils.horizontal_swipe_screen_once()

        BaseActionInfo.execute(self)

class CheckEnergyV2Info(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        notEnoughEnergy, _, _ = utils.patternDetect("no_enough_engergy_pattern.png")
        if notEnoughEnergy:
            hasAdsEnergy, _, _ = utils.patternDetect("energy_watch_ads_patten.png")
            if hasAdsEnergy > 0:
                # click the ads energy
                ScenarioExecutor("s6_watch_energy_ads.json").execute()
            elif utils.use_energy_ball > 0:
                hasEnergyBall, _, _ = utils.patternDetect("energy_ball_pattern.png")
                if hasEnergyBall > 0:
                    ScenarioExecutor("s6_use_energy_ball.json").execute()
                else:
                    sys.exit(0)
            else:
                sys.exit(0)
        else:
            return

        #nothing just return
        BaseActionInfo.execute(self)


class CheckEnergyNotEnough(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        hasAdsEnergy = utils.hasEnergyAds()
        if hasAdsEnergy > 0:
            # click the ads energy
            ScenarioExecutor("s6_watch_energy_ads.json").execute()
        else:
            hasEnergyBall = utils.hasEnergyBall()
            if hasEnergyBall > 0:
                ScenarioExecutor("s6_use_energy_ball.json").execute()

        #nothing just return
        BaseActionInfo.execute(self)

class CheckTooMany(BaseActionInfo):
    def __init__(self, message, sleepTime):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime

    def execute(self):
        hasTooManyWarning = utils.hasTooManyWarning()
        if hasTooManyWarning > 0:
            # click the ads energy
            ScenarioExecutor("s6_sell_all_useless.json").execute()
            hasTooManyWarning = utils.hasTooManyWarning()
            if hasTooManyWarning > 0:
                # need help
                sys.exit(0)
            return

        #nothing just return
        BaseActionInfo.execute(self)

class DetectPatternAction(BaseActionInfo):
    def __init__(self, message, sleepTime, pattern_file, detect_times, fallback_script):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime
        self.pattern_file = pattern_file
        self.detect_times = detect_times
        self.fallback_script = fallback_script

    def execute(self):
        BaseActionInfo.execute(self)
        containsPattern = 0
        for j in range(self.detect_times):
            print("Detect rounds {}!".format(j))
            containsPattern, _, _ = utils.patternDetect(self.pattern_file)
            if containsPattern > 0:
                break

        if containsPattern > 0:
            #found it.
            return
        else:
            if len(self.fallback_script) > 1:
                ScenarioExecutor(self.fallback_script).execute()

class DetectSharingAction(BaseActionInfo):
    def __init__(self, message, sleepTime, pattern_file, detect_times):
        BaseActionInfo.__init__(self,message, sleepTime)
        self.sleepTime = sleepTime
        self.pattern_file = pattern_file
        self.detect_times = detect_times

    def execute(self):
        BaseActionInfo.execute(self)
        containsPattern = 0
        for j in range(self.detect_times):
            print("Detect rounds {}!".format(j))
            utils.tap_screen(1760, 1030)
            utils.sleep_wait(1)
            containsPattern, _, _ = utils.patternDetect(self.pattern_file)
            if containsPattern > 0:
                break

        if containsPattern > 0:
            #found it.
            return
        else:
            print("No Sharing at all")
            sys.exit(0)

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
        elif actionName == "check_category":
            CheckCategoryInfo(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "check_energy":
            CheckEnergyNotEnough(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "check_too_many":
            CheckTooMany(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "check_energy_v2":
            CheckEnergyV2Info(self.jsonObject["message"], self.jsonObject["sleepTime"]).execute()
        elif actionName == "pattern_detect":
            DetectPatternAction(self.jsonObject["message"], self.jsonObject["sleepTime"], self.jsonObject["pattern_file"], self.jsonObject["detectTimes"], self.jsonObject["fallback_script"]).execute()
        elif actionName == "detect_sharing":
            DetectSharingAction(self.jsonObject["message"], self.jsonObject["sleepTime"], self.jsonObject["pattern_file"], self.jsonObject["detectTimes"]).execute()
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