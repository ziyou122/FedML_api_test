from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper

class GetUserInfoByToken(SequentialTaskSet):
    @task
    def fetch_user_information(self):
        header = UtilHelper.get_base_header_with_cookie(self.user.get_cookie())
        token = self.user.get_data()['token']
        header['token'] = token
        with self.client.get("/account/getCurrentAccount?token="+token, headers=header, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get user info, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get user info, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
