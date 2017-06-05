"""
弄一个最基础的类，然后方便后续统一修改和扩展
"""
import json
import unittest

import requests

domain = 'http://api.apiapp.cc'  # 接口测试的根域名


class MyBaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        一些参数设置
        """
        super(MyBaseTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass


class MyLoginBaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        一些参数设置
        """
        super(MyLoginBaseTest, self).__init__(*args, **kwargs)
        self.path = '%s/account' % domain

        url = self.path + '/user-login/'

        post_data = dict(
            user='test_user',
            password='asdf1234',
        )

        res = requests.post(url, data=json.dumps(post_data))
        print(res.text)

        res_json = json.loads(res.text)
        self.token = res_json['data']['token']

    def setUp(self):
        pass

    def tearDown(self):
        pass
