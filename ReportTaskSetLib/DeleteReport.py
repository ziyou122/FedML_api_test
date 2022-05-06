from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class DeleteReport(SequentialTaskSet):

    # # 删除刚创建的project
    @task
    def delete_report(self):
        print(self.user.get_data())
        form_data = {"report_id": 16}
        with self.client.delete(
                "/reports/deleteReport",
                json.dumps(form_data),
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
