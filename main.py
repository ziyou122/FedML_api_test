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

from ProjectTaskSetLib.CreateProject import CreateProject
from ProjectTaskSetLib.QueryProjectById import QueryProjectById
from ProjectTaskSetLib.QueryProjectByUserid import QueryProjectByUserid
from ProjectTaskSetLib.QueryProjectByGroupid import QueryProjectByGroupid
from ProjectTaskSetLib.TotalProjectTest import TotalProjectTest
from ProjectTaskSetLib.DeleteProject import DeleteProject
from ProjectTaskSetLib.QueryProjectByPage import QueryProjectByPage

from EdgeTaskSetLib.CreateEdge import CreateEdge
from EdgeTaskSetLib.UpdateEdge import UpdateEdge
from EdgeTaskSetLib.DeleteEdge import DeleteEdge
from EdgeTaskSetLib.BindDevice import BindDevice
from EdgeTaskSetLib.QueryEdgeById import QueryEdgeById
from EdgeTaskSetLib.QueryEdgeByUserId import QueryEdgeByUserid
from EdgeTaskSetLib.QueryUserByDeviceId import QueryUserByDeviceid
from EdgeTaskSetLib.TotalEdgeTest import TotalEdgeTest

from RunTaskSetLib.CreateRun import CreateRun
from RunTaskSetLib.UpdateRun import UpdateRun
from RunTaskSetLib.DeleteRun import DeleteRun
from RunTaskSetLib.QueryRunById import QueryRunById
from RunTaskSetLib.QueryRunByProjectid import QueryRunByProjectId
from RunTaskSetLib.QueryRunByGroupid import QueryRunByGroupid
from RunTaskSetLib.QueryRunByUserid import QueryRunByUserid
from RunTaskSetLib.TotalRunTest import TotalRunTest

from ChartTaskSetLib.CreateChart import CreateChart
from ChartTaskSetLib.DeleteChart import DeleteChart
from ChartTaskSetLib.UpdateChart import UpdateChart
from ChartTaskSetLib.QueryChartById import QueryChartById
from ChartTaskSetLib.QueryChartByPage import QueryChartByPage
from ChartTaskSetLib.QueryChartByUserid import QueryChartByUserid
from ChartTaskSetLib.TotalChartTest import TotalChartTest

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
    RegisteredHttpUser.tasks = [TotalChartTest]