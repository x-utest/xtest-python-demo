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
        self.assertEqual(code, 200, msg='能够正常的插入返回值')

        remote_ip = res_json.get('data').get('remote_ip', None)
        self.assertNotEqual(remote_ip, None, msg='可以获取到客户端的IP地址')
