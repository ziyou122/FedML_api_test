from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper

class TotalGroupTest(SequentialTaskSet):
    @task
    def create_group(self):
        uid = self.user.get_data()['id']
        form_data = {'name': "test_Ziyou_" + str(UtilHelper.get_random_string(10)), 'userids': [uid]}

        with self.client.post(
                "/groups",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create group, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_group(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create group, Text: " + response.text)

    @task
    def update_group(self):
        gid = self.user.get_group()
        uid = self.user.get_data()['id']
        form_data = {'id': gid}

        with self.client.put(
                "/groups",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to update group, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to update group, Text: " + response.text)

    @task
    def query_group_by_id(self):
        with self.client.get(
                "/groups?id="+str(self.user.get_group()),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get group by group id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get group by group id, Text: " + response.text)

    @task
    def query_group_by_UserId(self):

        with self.client.get(
                "/groups/user?id=" + str(self.user.get_data()['id']),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

    @task
    def delete_group(self):
        with self.client.delete(
                "/groups?id="+str(self.user.get_remove_group()),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to delete group, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete group, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
