from locust import task, SequentialTaskSet
import json
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class TotalEdgeTest(SequentialTaskSet):
    # 1.bind device 2. create edge 3. update edge
    # 4. query by id 5. query by group id 6. query by user id 7. query by device id 8. query by run id
    # 9.delete edge 10. unbound device

    # 1. bind device
    @task
    def bind_device(self):
        uid = self.user.get_data()['id']
        form_data = {'accountid': uid, 'deviceid': '1'}
        with self.client.post(
                "/edges/binding",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                # print(response.text)
                response.failure("Failed to get group by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get group by user id, Text: " + response.text)

    # 2. create a new edge
    @task
    def create_edge(self):
        uid = self.user.get_data()['id']
        form_data = {'name': "edge_test_"+str(UtilHelper.get_random_string(5)), 'accountid': uid, 'deviceid': '1'}

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

    # 3. update this edge
    @task
    def update_edge(self):
        eid = self.user.get_edge()
        form_data = {'id': eid}

        with self.client.put(
                "/edges",
                json.dumps(form_data),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to update edge, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to update edge, Text: " + response.text)


    # 4. query edge by edge id
    @task
    def query_edge_by_id(self):
        eid = self.user.get_edge()

        with self.client.get(
                "/edges?id=" + str(eid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get edge by edge id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get edge by edge id, Text: " + response.text)

    # 5 query edge by group id
    @task
    def query_edge_by_groupid(self):
        print('query edge by group id......')
        #   TODO

    # 6 query edge by user id
    @task
    def query_edge_by_userid(self):
        uid = self.user.get_data()['id']

        with self.client.get(
                "/edges/user?id=" + str(uid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get edge by user id, StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get edge by user id, Text: " + response.text)

    # 7. query edge by device id
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
                    response.success()
                else:
                    response.failure("Failed to get edge by device id, Text: " + response.text)

    # 8. query edge by run id
    @task
    def query_edge_by_runid(self):
        print("query edge by run id......")
        # TODO

    # 9.delete this edge
    @task
    def delete_edge(self):
        eid = self.user.get_edge()

        with self.client.delete(
                "/edges?id=" + str(eid),
                headers=UtilHelper.get_base_header_with_authorization(self.user.get_data()['token']),
                catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to delete edge StatusCode: " + str(response.status_code))
            else:
                if "SUCCESS" in response.text:
                    response.success()
                else:
                    response.failure("Failed to delete edge, Text: " + response.text)

    # 10 unbound device
    @task
    def unbound_device(self):
        print("unbound device......")
        # TODO

    @task
    def exit_task_execution(self):
        self.interrupt()