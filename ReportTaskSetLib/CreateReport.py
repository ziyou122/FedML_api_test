from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CreateReport(SequentialTaskSet):
    @task
    def create_report(self):
        uid = self.user.get_data()['id']
        form_data = {'project_id': '208',
                     'created_by': uid,
                     'updated_by': uid,
                     'report_name': 'report_test'+str(UtilHelper.get_random_string(5)),
                     'sections': [{'section_name': "Training charts", 'runs': [], 'isTableShow': 'true', 'charts': []}]
                     }

        with self.client.post(
                "/reports/createReport",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create report, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to create report, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()