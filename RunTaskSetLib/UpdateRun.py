from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class UpdateRun(SequentialTaskSet):

    @task
    def update_run(self):
        form_data = {'id': 834}

        with self.client.put(
                "/runs",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to update run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    response.success()
                else:
                    response.failure("Failed to update run, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()