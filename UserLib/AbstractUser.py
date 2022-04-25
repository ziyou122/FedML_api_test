from locust import HttpUser

class AbstractUser(HttpUser):
    abstract = True

    def __init__(self, parent):
        super(AbstractUser, self).__init__(parent)
        self.user_attr = {}

    def set_name(self, email):
        self.user_attr['name'] = email

    def get_name(self):
        if 'name' in self.user_attr.keys():
            return self.user_attr['name']
        else:
            return None

    def set_cookie(self, cookie):
        self.user_attr['cookie'] = cookie

    def get_cookie(self):
        return self.user_attr['cookie']

    # 保存登录时的用户信息
    def set_data(self, data):
        self.user_attr['data'] = data

    def get_data(self):
        return self.user_attr['data']

    # 保存用户的详细信息
    def set_detailed_data(self, data):
        self.user_attr['detailed_data'] = data

    def get_detailed_data(self):
        return self.user_attr['detailed_data']

    # 保存group id
    def set_group(self, data):
        if 'group_id' not in self.user_attr:
            self.user_attr['group_id'] = []
        self.user_attr['group_id'].append(data)

    def get_group(self):
        return self.user_attr['group_id'][-1]

    def get_remove_group(self):
        return self.user_attr['group_id'].pop()

    def set_project(self, data):
        self.user_attr['project_id'] = data

    def get_project(self):
        return self.user_attr['project_id']