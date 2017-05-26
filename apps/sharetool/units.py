"""
sharetool模块的测试脚本
"""
import json

import requests

from apps.my_base import MyBaseTest, domain


class ShareToolApi(MyBaseTest):
    def setUp(self):
        self.path = '%s/sharetool' % domain  # 本模块的相对路径

    def test_get_client_info(self):
        """
        获取客户端信息的接口
        :return: 
        """
        url = self.path + '/get-client-info/'

        res = requests.get(url)
        res_json = json.loads(res.text)

        # 只写最简单的,后面再不断完善用例

        code = res_json.get('code', None)
        self.assertEqual(code, 200, msg='能够正常接受请求')

        remote_ip = res_json.get('data').get('remote_ip', None)
        self.assertNotEqual(remote_ip, None, msg='可以获取到客户端的IP地址')

    def test_async_sleep_demo(self):
        """
        这是一个异步的强行sleep个1s的接口
        :return: 
        """
        url = self.path + '/async-sleep-demo/'

        res = requests.get(url)
        res_json = json.loads(res.text)

        # 只写最简单的,后面再不断完善用例

        code = res_json.get('code', None)
        self.assertEqual(code, 200, msg='能够正常接受请求')

    def test_sync_sleep_demo(self):
        """
        这是一个同步的强行sleep个1s的接口
        :return: 
        """
        url = self.path + '/sync-sleep-demo/'

        res = requests.get(url)
        res_json = json.loads(res.text)

        # 只写最简单的,后面再不断完善用例

        code = res_json.get('code', None)
        self.assertEqual(code, 200, msg='能够正常接受请求')

    def test_just_now_demo(self):
        """
        这是一个立刻就返回的接口
        :return: 
        """
        url = self.path + '/just-now-handler/'

        res = requests.get(url)
        res_json = json.loads(res.text)

        # 只写最简单的,后面再不断完善用例

        code = res_json.get('code', None)
        self.assertEqual(code, 200, msg='能够正常接受请求')

