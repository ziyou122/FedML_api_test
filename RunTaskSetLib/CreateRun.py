from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CreateRun(SequentialTaskSet):
    @task
    def query_project_by_userid(self):
        uid = self.user.get_data()['id']

        with self.client.get(
                "/projects/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_project(eval(response.text)['data'][0]['id'])
                    response.success()
                else:
                    response.failure("Failed to get project by user id, Text: " + response.text)

    @task
    def create_run(self):
        pid = self.user.get_project()
        uid = self.user.get_data()['id']
        form_data = {'projectid': pid, 'name': "run_test_"+str(UtilHelper.get_random_string(5)), 'urls': {}}

        with self.client.post(
                "/runs",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to create run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to create run, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()