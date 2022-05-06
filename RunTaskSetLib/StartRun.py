from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CreateRun(SequentialTaskSet):

    @task
    def start_run(self):
        pid = self.user.get_project()
        uid = self.user.get_data()['id']
        gid = self.user.get_group();
        form_data = {'groupid': gid, 'name': "run_test_"+str(UtilHelper.get_random_string(5)), 'urls': {}}

        with self.client.post(
                "/runs/start",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to start run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to start run, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()