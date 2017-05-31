import json

import requests

from apps.my_base import MyBaseTest, domain


class AccountApi(MyBaseTest):
    """
    服务端的基础接口
    """

    def setUp(self):
        self.path = '%s/account' % domain  # 本模块的相对路径

    def test_home_page(self):
        """
        用户注册接口测试，用户登录测试
        :return:
        """
        url = self.path + '/create-new-user/'

        post_data = dict(
            user='user544',
            password='password',
            u_name='xtst user'
        )

        res = requests.post(url, data=json.dumps(post_data))

        code = res.status_code
        self.assertEqual(code, 200, msg='这个服务器home页面要有返回值')
