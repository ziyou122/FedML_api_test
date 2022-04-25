from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class BindDevice(SequentialTaskSet):
    @task
    def bind_device(self):
        uid = self.user.get_data()['id']
        form_data = {'accountid': uid, 'deviceid': '1'}
        with self.client.post(
                "/edges/binding",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                print(response.text)
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print("true")
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()