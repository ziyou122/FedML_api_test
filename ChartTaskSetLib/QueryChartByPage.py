from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper
import json


# query by page 没有调试成功
class QueryChartByPage(SequentialTaskSet):
    @task
    def query_chart_by_page(self):
        form_data = {'page': '1'}
        with self.client.post(
                "/charts/group",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to get chart by page, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get chart by page, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
