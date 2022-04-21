from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class QueryGroupByUserId(SequentialTaskSet):
    @task
    def query_group_by_UserId(self):

        with self.client.get(
                "/groups/user?id="+str(self.user.get_data()['id']),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
