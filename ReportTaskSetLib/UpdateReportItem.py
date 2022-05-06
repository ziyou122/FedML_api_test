from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class UpdateReportItems(SequentialTaskSet):
    @task
    def update_report_details(self):
        form_data = {"report_id":'30',"report_name":"Report new","project_id":'208'}
        with self.client.put(
                "/reports/updateReport",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
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
