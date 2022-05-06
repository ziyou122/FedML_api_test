from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class AddContact(SequentialTaskSet):

    @task
    def add_contact(self):
        uid = self.user.get_data()['id']
        form_data = {'userid':uid}

        with self.client.post(
                "/contact",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
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