from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class UpdateReportDetails(SequentialTaskSet):
    @task
    def update_report_details(self):
        form_data = {"created_by":199,"updated_by":199,"report_name":"report_testlsqgg","project_id":"208","report_id":19,"update_time":1651687066000,"sections":[{"charts":[],"update_time":1651687066000,"create_time":1651687066000,"report_id":"19","section_name":"Training charts","updated_by":"199","id":34,"created_by":"199","runs":[]}]}
        with self.client.put(
                "/reports/updateReportDetails",
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
