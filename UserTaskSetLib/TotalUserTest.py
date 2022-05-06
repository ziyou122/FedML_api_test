import json

from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class TotalUserTest(SequentialTaskSet):
    # get user info by token
    # query user info by user id
    # query user friends by user id
    # query user info by user name
    # update user info
    # update user avatar     X
    # modify user password   X
    @task
    def get_user_info_by_token(self):
        token = self.user.get_data()['token']
        with self.client.get("/account/getCurrentAccount?token=" + token, headers=UtilHelper.get_base_header_json(),
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get user info, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get user info, Text: " + response.text)

    @task
    def query_user_by_userid(self):
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
    def query_friends_by_userid(self):
        uid = self.user.get_data()['id']
        with self.client.get(
                "/account/friends?key=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to query firends by usesid, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to query firends by usesid, Text: " + response.text)

    @task
    def fetch_user_info_by_username(self):

        account = self.user.get_data()['account']
        with self.client.get(
                "/account/name?account=" + str(account),
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
    def update_user_information(self):
        old_user_info = self.user.get_detailed_data()
        # 更新用户信息，这里没有实质更新
        new_user_info = old_user_info
        with self.client.post(
                "/account/updateUser",
                json.dumps(new_user_info[0]),
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
