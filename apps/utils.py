import json

import requests

from apps.my_base import domain


def get_project_version():
    """
    获取服务端的版本信息
    1. 要求服务端必须提供此动态接口
    :return: 
    """

    url = '%s/app-info/' % domain
    res = requests.get(url)

    if res.status_code != 200:
        return None

    res_json = json.loads(res.text)
    app_version = res_json.get('data').get('app_version', None)
    return app_version



