import json

import requests

from apps.my_base import MyBaseTest, domain, MyLoginBaseTest


class AnoymousAccountApi(MyBaseTest):
    """
    匿名非登录接口服务端的基础接口
    """

    def setUp(self):
        self.path = '%s/account' % domain  # 本模块的相对路径

    # def test_create_user(self):
    #     """
    #     用户注册接口测试，用户登录测试
    #     :return:
    #     """
    #     url = self.path + '/create-new-user/'
    #
    #     post_data = dict(
    #         user='test_user',
    #         password='asdf1234',
    #         u_name='xtst-user'
    #     )
    #
    #     res = requests.post(url, data=json.dumps(post_data))
    #
    #     code = res.status_code
    #     self.assertEqual(code, 200, msg='这个服务器home页面要有返回值')

    def test_user_login(self):
        """
        用户注册接口测试，用户登录测试
        :return:
        """
        url = self.path + '/user-login/'

        post_data = dict(
            user='test_user',
            password='asdf1234',
        )

        res = requests.post(url, data=json.dumps(post_data))
        print(res.text)

        res_json = json.loads(res.text)
        self.token = res_json['data']['token']

        code = res.status_code
        self.assertEqual(code, 200, msg='这个服务器home页面要有返回值')

    def test_user_logout(self):
        """
        测试用户登出
        :return: 
        """
        url = self.path + '/user-login/'
        get_data = dict(
            user='test_user',
            password='asdf1234',
        )
        res = requests.post(url, data=json.dumps(get_data))
        res_json = json.loads(res.text)
        token = res_json['data']['token']

        logout_url = self.path + '/user-logout/'

        get_data = dict(
            token=token
        )

        res = requests.get(logout_url, params=get_data)
        print(res.text)

        code = json.loads(res.text).get('code', None)
        self.assertEqual(code, 200, msg='这个服务器home页面要有返回值')


class LoginAccountApi(MyLoginBaseTest):
    """
    登录之后的账号的接口
    """

    # todo 后面就大量的写这里面的接口了
    def setUp(self):
        pass
        # self.token = None  # 登录后换取的token

    def test_login_api(self):
        self.assertFalse(True, msg='只是做个测试init')
