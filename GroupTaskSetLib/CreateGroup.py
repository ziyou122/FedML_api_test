from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CreateGroup(SequentialTaskSet):
    @task
    def create_group(self):
        uid = self.user.get_data()['id']
        form_data = {'name': "test_Ziyou_"+str(UtilHelper.get_random_string(10)), 'userids': [uid]}

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
    def exit_task_execution(self):
        self.interrupt()
