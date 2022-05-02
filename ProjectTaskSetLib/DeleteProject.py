from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class DeleteProject(SequentialTaskSet):
    # 先查询当前user下的group，并存储
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

    # 根据存储的group id创建project,存储project id
    @task
    def create_project(self):
        gid = self.user.get_group();
        uid = self.user.get_data()['id']
        form_data = {'groupid': gid, 'name': "project_test_" + str(UtilHelper.get_random_string(5)), 'userid': uid}

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

    # # 删除刚创建的project
    @task
    def delete_group(self):
        pid = self.user.get_project()
        with self.client.delete(
                "/projects?id="+str(pid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to delete group, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    response.success()
                else:
                    response.failure("Failed to delete group, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
