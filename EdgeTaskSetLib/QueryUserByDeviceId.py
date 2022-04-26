from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class QueryUserByDeviceid(SequentialTaskSet):
    @task
    def query_edge_by_deviceid(self):

        with self.client.get(
                "/edges/device?id=1",
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get edge by device id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    response.success()
                else:
                    response.failure("Failed to get edge by device id, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
