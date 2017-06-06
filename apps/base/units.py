import json

import requests

from apps.my_base import MyBaseTest, domain


class BaseApi(MyBaseTest):
    """
    服务端的基础接口
    """

    def setUp(self):
        self.path = '%s' % domain  # 本模块的相对路径

    def test_home_page(self):
        """
        测试服务端的home页面是否有返回值
        :return: 
        """
        url = self.path + '/'
        res = requests.get(url)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)

    def test_web_info_api(self):
        """
        用来测试 api服务是否有版本信息接口
        :return: 
        """
        url = self.path + '/app-info/'
        res = requests.get(url)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)
        res_json = json.loads(res.text)
        app_version = res_json.get('data').get('app_version', None)
        self.assertNotEqual(app_version, None, msg='这个服务器里面必须要有这个接口')

    def test_feedback(self):
        """
        测试反馈接口
        :return: 
        """
        url = self.path + "/feedback/"

        # 插入正常值
        post_data = dict(
            msg='测试数据插入'
        )

        res = requests.post(url, data=post_data)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)

        # 插入空字符串
        post_data = dict(
            msg=''
        )
        res = requests.post(url, data=post_data)
        res_json = json.loads(res.text)
        code = res_json.get('code', None)
        self.assertEqual(code, 400, msg='插入空字符串是不被接受的')
