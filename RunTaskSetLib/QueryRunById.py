from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class QueryRunById(SequentialTaskSet):
    @task
    def query_run_by_id(self):

        with self.client.get(
                "/runs?id=835",
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to get run by run id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get run by run id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
