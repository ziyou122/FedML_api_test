from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class TotalRunTest(SequentialTaskSet):
    # 1.create run 2.query run by id 3.query run by user id 4.query run by group id
    # 5.query run by project id 6.update run 7.start run 8.stop run 9.run callback
    # 10.delete run
    @task
    def query_project_by_userid(self):
        uid = self.user.get_data()['id'];
        with self.client.get(
                "/projects/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get project by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_project(eval(response.text)['data'][0]['id'])
                    response.success()
                else:
                    response.failure("Failed to get project by user id, Text: " + response.text)

    @task
    def create_run(self):
        pid = self.user.get_project()
        form_data = {'projectid': pid, 'name': "run_test_"+str(UtilHelper.get_random_string(5)), 'urls': {}}

        with self.client.post(
                "/runs",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_run(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create run, Text: " + response.text)

    @task
    def query_run_by_id(self):
        rid = self.user.get_run()
        with self.client.get(
                "/runs?id=" + str(rid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get run by run id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_group(eval(response.text)['data']['groupid'])
                    self.user.set_project(eval(response.text)['data']['projectid'])
                    response.success()
                else:
                    response.failure("Failed to get run by run id, Text: " + response.text)

    @task
    def query_run_by_userid(self):
        uid = self.user.get_data()['id']
        with self.client.get(
                "/runs/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get run by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get run by user id, Text: " + response.text)

    @task
    def query_run_by_groupid(self):
        gid = self.user.get_group()
        with self.client.get(
                "/runs/group?id=" + str(gid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

    @task
    def query_run_by_projectid(self):
        pid = self.user.get_project()
        with self.client.get(
                "/runs/project?id=" + str(pid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get run by project id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get run by project id, Text: " + response.text)

    @task
    def update_run(self):
        rid = self.user.get_run()
        form_data = {'id': rid}

        with self.client.put(
                "/runs",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to update run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to update run, Text: " + response.text)

    @task
    def create_edge(self):
        uid = self.user.get_data()['id']
        form_data = {'name': "edge_test_" + str(UtilHelper.get_random_string(5)), 'accountid': uid, 'deviceid': '1'}

        with self.client.post(
                "/edges",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create edge, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    self.user.set_edge(eval(response.text)['data'])
                    response.success()
                else:
                    response.failure("Failed to create edge, Text: " + response.text)

    @task
    def start_run(self):
        pid = self.user.get_project()
        # uid = self.user.get_data()['id']
        gid = self.user.get_group()
        eid = self.user.get_edge()
        form_data = {'projectid': pid, 'groupid': gid, 'name': "run_test_" + str(UtilHelper.get_random_string(5)), 'urls': {}, 'edgeids': [eid]}

        with self.client.post(
                "/runs/start",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to create run, Text: " + response.text)

    @task
    def stop_run(self):
        rid = self.user.get_run()
        form_data = {'key': rid, 'server': '', 'servertype':''}

        with self.client.post(
                "/runs/stop",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to stop run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to stop run, Text: " + response.text)

    @task
    def run_callback(self):
        rid = self.user.get_run()
        form_data = {'key': rid, 'server': '', 'servertype': ''}

        with self.client.post(
                "/runs/runCallback",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to run callback, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to run callback, Text: " + response.text)

    @task
    def delete_run(self):
        rid = self.user.get_run()
        with self.client.delete(
                "/runs?id=" + str(rid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to delete run, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete run, Text: " + response.text)

    @task
    def delete_edge(self):
        # eid = self.user.get_edge()

        with self.client.delete(
                "/edges?id=127",
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to delete edge StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete edge, Text: " + response.text)

    @task
    def exit_task_execution(self):
        self.interrupt()