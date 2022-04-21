from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper
import os

class UploadUserAvatar(SequentialTaskSet):
    @task
    def upload_avatar(self):
        with open(os.path.dirname(__file__)+"\\..\\Data\\img_avatar.png", "rb") as f:
            img_bin = f.read()

        data = {'file': img_bin}
        with self.client.post(
                "/account/avatar", data, headers=UtilHelper.get_base_header_with_authorization(self.user.get_token()), catch_response=True) as response:
            if response.status_code != 200:
                print(response.request.headers)
                print(response.text)
                response.failure("Failed to upload avatar, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to upload avatar, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
