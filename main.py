from locust import events

from UserLib.RegisteredHttpUser import RegisteredHttpUser
from CommonLib.UserLoader import UserLoader
from CommonLib.LogModule import Logger
from CommonLib.EventHandlers import EventHandlers

from UserTaskSetLib.GetUserInfoByToken import GetUserInfoByToken
from UserTaskSetLib.UploadUserAvatar import UploadUserAvatar
from UserTaskSetLib.QueryUserById import QueryUserById
from UserTaskSetLib.QueryUserByName import QueryUserByName
from UserTaskSetLib.QueryUserFriendsById import QueryUserFriendsById
from UserTaskSetLib.UpdateUserInfo import UpdateUserInfo

from GroupTaskSetLib.CreateGroup import CreateGroup
from GroupTaskSetLib.DeleteGroup import DeleteGroup
from GroupTaskSetLib.QueryGroupById import QueryGroupById
from GroupTaskSetLib.QueryGroupByUserId import QueryGroupByUserId
from GroupTaskSetLib.TotalGroupTest import TotalGroupTest

@events.test_start.add_listener
def on_test_start(**kwargs):
    if kwargs['environment'].parsed_options.logfile:
        Logger.init_logger(__name__, kwargs['environment'].parsed_options.logfile)
    UserLoader.load_users()
    Logger.log_message("......... Initiating Test .......")

@events.test_stop.add_listener
def on_test_stop(**kwargs):
    Logger.log_message("........ Test Completed ........")



class UserGroupA(RegisteredHttpUser):
    weight = 1
    RegisteredHttpUser.tasks = [TotalGroupTest]