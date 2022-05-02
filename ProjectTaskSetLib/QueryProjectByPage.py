from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper
import json

# query by page 没有调试成功
class QueryProjectByPage(SequentialTaskSet):
    @task
    def query_project_by_page(self):
        form_data = {'page': 1}
        with self.client.post(
                "/projects/group",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by page, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get project by page, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()
