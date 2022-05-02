from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CreateChart(SequentialTaskSet):

    @task
    def create_chart(self):
        uid = self.user.get_data()['id']
        form_data = {'account_id': uid}

        with self.client.post(
                "/charts",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to create chart, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to create chart, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()