from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper

class UpdateUserInfo(SequentialTaskSet):

    @task
    def fetch_user_information(self):
        print('----------fetch--------------')
        uid = self.user.get_data()['id']
        with self.client.get(
                "/account/users?userKeys=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to upload avatar, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_detailed_data(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to upload avatar, Text: " + response.text)

    @task
    def update_user_information(self):
        print('----------update--------------')
        old_user_info = self.user.get_detailed_data()
        # 更新用户信息，这里没有更新
        new_user_info = old_user_info
        with self.client.post(
                "/account/updateUser",
                new_user_info,
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to upload avatar, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to upload avatar, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
