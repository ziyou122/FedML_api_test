from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class TotalReportTest(SequentialTaskSet):
    @task
    def query_project_by_userid(self):
        uid = self.user.get_data()['id']

        with self.client.get(
                "/projects/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by project id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_project(eval(response.text)['data'][0]['id'])
                    response.success()
                else:
                    response.failure("Failed to get project by project id, Text: " + response.text)

    @task
    def create_report(self):
        uid = self.user.get_data()['id']
        pid = self.user.get_project()
        form_data = {'project_id': pid,
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
                    self.user.set_report(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create report, Text: " + response.text)

    @task
    def get_report_list(self):
        pid = self.user.get_project()
        form_data = {"project_id": pid, "num_per_page": 999, "requst_page_num": 1}
        with self.client.post(
                "/reports/getReportList",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get report list, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get report list, Text: " + response.text)

    @task
    def update_report_details(self):
        uid = self.user.get_data()['id']
        rid = self.user.get_report()
        pid = self.user.get_project()
        form_data = {"created_by": uid, "updated_by": uid, "report_name": "report_test_updated", "project_id": pid,
                     "report_id": rid, "update_time": 1651687066000, "sections": [
                {"charts": [], "update_time": 1651687066000, "create_time": 1651687066000, "report_id": rid,
                 "section_name": "Training charts", "updated_by": uid, "id": 34, "created_by": uid, "runs": []}]}
        with self.client.put(
                "/reports/updateReportDetails",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            # print(response.text)
            if response.status_code != 200:
                response.failure("Failed to update project details, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to g update project details, Text: " + response.text)

    # internal error
    @task
    def update_report(self):
        rid = self.user.get_report()
        pid = self.user.get_project()
        form_data = {"report_id": rid, "report_name": "Report new", "project_id": pid}
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

    # error
    @task
    def delete_report(self):
        rid = self.user.get_report()
        form_data = {"report_id": rid}
        with self.client.delete(
                "/reports/deleteReport",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to delete group, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete group, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()