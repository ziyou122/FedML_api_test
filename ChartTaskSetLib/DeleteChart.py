from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class DeleteChart(SequentialTaskSet):
    @task
    def delete_chart(self):
        with self.client.delete(
                "/charts?id="+str(72),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to delete chart, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete chart, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
