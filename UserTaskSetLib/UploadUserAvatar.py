from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper
import os
import json

class UploadUserAvatar(SequentialTaskSet):
    @task
    def upload_avatar(self):
        with open(os.path.dirname(__file__)+"\\..\\Data\\img_avatar.png", "rb") as f:
            img_bin = f.read()

        data = {'file': str(img_bin)}
        with self.client.post(
                "/files/upload",
                json.dumps(data),
                headers=UtilHelper.get_multipart_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to upload avatar, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to upload avatar, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
