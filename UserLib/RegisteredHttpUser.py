from locust import between, clients
from locust.exception import StopUser
import json

from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper
from CommonLib.UserLoader import UserLoader
from UserLib.AbstractUser import AbstractUser

class RegisteredHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True

    def verify_login_success(self, response, email):
        if response.status_code != 200 or 'Authentication failed.' in response.text:
            response.failure("Failed to login, user: " + email + " Status Code : " + str(response.status_code))
            raise StopUser()
        return True

    def on_start(self):
        # fetch a use from user list file and then login
        user_obj = UserLoader.get_user()
        form_data = {'name': user_obj['username'], 'password': user_obj['password']}
        with self.client.post(
                "/account/login",
                form_data,
                headers=UtilHelper.get_base_header(),
                catch_response=True) as response:
            if self.verify_login_success(response, user_obj['username']):
                Logger.log_message("Login successful with user : " + user_obj['username'], LogType.INFO)
                # print(response.text)
                super().set_data(eval(response.text)['data'])
                super().set_name(user_obj['username'])
                super().set_cookie(response.cookies)

    def on_stop(self):
        with self.client.get(
                "/account/logout",
                headers=UtilHelper.get_base_header_with_authorization(super().get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to logout, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to logout, Text: " + response.text)
        print('RegisteredHttpUser: stop')