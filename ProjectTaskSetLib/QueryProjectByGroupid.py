from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class QueryProjectByGroupid(SequentialTaskSet):
    @task
    def query_project_by_groupid(self):
        uid = self.user.get_data()['id']
        gid = 0
        with self.client.get(
                "/groups/user?id="+str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    gid = eval(response.text)['data'][0]['id']
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

        with self.client.get(
                "/projects/group?id=" + str(gid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by group id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    response.success()
                else:
                    response.failure("Failed to get project by group id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
