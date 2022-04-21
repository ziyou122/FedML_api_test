import random
import string
from datetime import datetime


class UtilHelper:

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def get_current_time_stamp():
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        return timestamp

    @staticmethod
    def get_base_header():
        base_header = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive'
        }
        return base_header

    @staticmethod
    def get_base_header_json():
        base_header = {
            'Content-type': 'application/json',
            'Connection': 'keep-alive'
        }
        return base_header

    @staticmethod
    def get_multipart_header():
        base_header = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
            'Content-type': 'multipart/form-data; boundary=----WebKitFormBoundary'+str(random.randint(1e28, 1e29 - 1)),
            'ignorecanceltoken': 'true',
            'origin': 'https://open.fedml.ai',
            'refer': 'https://open.fedml.ai/'
        }
        return base_header

    @staticmethod
    def get_base_header_with_cookie(cookie):
        cookie_header = UtilHelper.get_base_header()
        cookie_str = ""
        for item in cookie.iteritems():
            cookie_str += item[0] + "=" + item[1]
        cookie_header['Cookie'] = cookie_str
        return cookie_header

    @staticmethod
    def get_base_header_with_authorization(token):
        authorization_header = UtilHelper.get_base_header_json()
        authorization_header['authorization'] = token
        return authorization_header
