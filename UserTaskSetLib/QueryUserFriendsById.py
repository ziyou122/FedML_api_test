from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper

class QueryUserFriendsById(SequentialTaskSet):
    @task
    def fetch_user_information(self):

        uid = self.user.get_data()['id']
        with self.client.get(
                "/account/friends?key="+str(uid), headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']), catch_response=True) as response:
            if response.status_code != 200:
                print(response.text)
                response.failure("Failed to upload avatar, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to upload avatar, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
