from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class UpdateEdge(SequentialTaskSet):

    @task
    def update_edge(self):
        eid = self.user.get_edge()
        form_data = {'id': eid}

        with self.client.put(
                "/edges",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to update edge, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to update edge, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()