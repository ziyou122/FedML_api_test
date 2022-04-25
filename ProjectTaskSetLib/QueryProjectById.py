from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class QueryProjectById(SequentialTaskSet):
    @task
    def query_project_by_id(self):

        with self.client.get(
                "/projects?id=180",
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by project id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    response.success()
                else:
                    response.failure("Failed to get project by project id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
