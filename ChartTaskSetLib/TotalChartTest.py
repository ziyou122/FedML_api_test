from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class TotalChartTest(SequentialTaskSet):

    @task
    def create_chart(self):
        uid = self.user.get_data()['id']
        form_data = {'account_id': uid}

        with self.client.post(
                "/charts",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to create chart, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_chart(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create chart, Text: " + response.text)

    @task
    def query_chart_by_id(self):
        cid = self.user.get_chart()
        with self.client.get(
                "/charts?id="+str(cid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to get chart by chart id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get chart by chart id, Text: " + response.text)

    @task
    def query_run_by_userid(self):
        uid = self.user.get_data()['id']
        with self.client.get(
                "/charts/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to get chart by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get chart by user id, Text: " + response.text)

    # failed 404
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
    def update_chart(self):
        cid = self.user.get_chart()
        form_data = {'id': cid}

        with self.client.put(
                "/charts",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to update chart, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    print(response.text)
                    response.success()
                else:
                    response.failure("Failed to update chart, Text: " + response.text)

    @task
    def delete_chart(self):
        cid = self.user.get_chart()
        with self.client.delete(
                "/charts?id=" + str(cid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            print(response.text)
            if response.status_code != 200:
                response.failure("Failed to delete chart, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete chart, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()