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

        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)

        # 详细的业务数据层次的测试
        res_json = json.loads(res.text)
        remote_ip = res_json.get('data').get('remote_ip', None)
        self.assertNotEqual(remote_ip, None, msg='可以获取到客户端的IP地址')

    def test_async_sleep_demo(self):
        """
        这是一个异步的强行sleep个1s的接口
        :return: 
        """
        url = self.path + '/async-sleep-demo/'

        res = requests.get(url)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)

    def test_sync_sleep_demo(self):
        """
        这是一个同步的强行sleep个1s的接口
        :return: 
        """
        url = self.path + '/sync-sleep-demo/'

        res = requests.get(url)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)

    def test_just_now_demo(self):
        """
        这是一个立刻就返回的接口
        :return: 
        """
        url = self.path + '/just-now-handler/'

        res = requests.get(url)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)
