from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CreateEdge(SequentialTaskSet):

    @task
    def create_edge(self):
        uid = self.user.get_data()['id']
        form_data = {'name': "edge_test_"+str(UtilHelper.get_random_string(5)), 'accountid': uid, 'deviceid': '1'}

        with self.client.post(
                "/edges",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create edge, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    self.user.set_edge(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create edge, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()