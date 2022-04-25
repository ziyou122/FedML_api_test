from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class TotalProjectTest(SequentialTaskSet):
    @task
    def query_group_by_UserId(self):

        with self.client.get(
                "/groups/user?id=" + str(self.user.get_data()['id']),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_group(eval(response.text)['data'][0]['id'])
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

    @task
    def create_project(self):
        gid = self.user.get_group()
        uid = self.user.get_data()['id']
        form_data = {'groupid': gid, 'name': "project_test_"+str(UtilHelper.get_random_string(5)), 'userid': uid}

        with self.client.post(
                "/projects",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create project, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_project(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create project, Text: " + response.text)

    @task
    def query_project_by_groupid(self):
        gid = self.user.get_group()
        with self.client.get(
                "/projects/group?id=" + str(gid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by group id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    # print(response.text)
                    response.success()
                else:
                    response.failure("Failed to get project by group id, Text: " + response.text)

    @task
    def query_project_by_id(self):
        pid = self.user.get_project()

        with self.client.get(
                "/projects?id=" + str(pid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by project id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    # print('by id')
                    # print(response.text)
                    response.success()
                else:
                    response.failure("Failed to get project by project id, Text: " + response.text)

    @task
    def query_project_by_userid(self):
        uid = self.user.get_data()['id']

        with self.client.get(
                "/projects/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by project id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    # print('by user id')
                    # print(response.text)
                    response.success()
                else:
                    response.failure("Failed to get project by project id, Text: " + response.text)

    @task
    def query_project_by_page(self):
        print('query project by page......')
        #   TODO

    @task
    def update_project(self):
        print("update project......")
        # TODO

    @task
    def delete_project(self):
        print("delete project......")
        # TODO


    @task
    def exit_task_execution(self):
        self.interrupt()