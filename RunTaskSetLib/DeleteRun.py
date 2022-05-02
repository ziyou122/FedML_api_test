from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class DeleteRun(SequentialTaskSet):
    @task
    def delete_run(self):
        with self.client.delete(
                "/runs?id="+str(835),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to delete run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete run, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
