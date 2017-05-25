import json

import requests

from apps.my_base import MyBaseTest, domain


class BaseApi(MyBaseTest):
    """
    服务端的基础接口
    """

    def test_web_info_api(self):
        """
        用来测试 api服务是否有版本信息接口
        :return: 
        """
        url = '%s/app-info/' % domain
        res = requests.get(url)
        res_json = json.loads(res.text)
        app_version = res_json.get('data').get('app_version', None)
        self.assertNotEqual(app_version, None, msg='这个服务器里面必须要有这个接口')