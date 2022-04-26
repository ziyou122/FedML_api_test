from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class QueryEdgeById(SequentialTaskSet):
    @task
    def query_edge_by_id(self):
        eid = self.user.get_edge()

        with self.client.get(
                "/edges?id=" + str(eid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            # print(response.text)
            if response.status_code != 200:
                response.failure("Failed to get project by project id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get project by project id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
