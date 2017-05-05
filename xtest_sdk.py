"""
测试报告生成的引用库

- 极验验证 www.geetest.com
- 支持python3.x
"""
import json
import requests


def dict_encode_test_results(test_results, **kwargs):
    """
    将pyunit中的测试结果进行数据提取和json编码
    :param test_results:
    :type test_results:  unittest.TestResult
    :return:
    """

    run_time = kwargs.get('run_time', None)
    pro_id = kwargs.get('pro_id', None)
    pro_version = kwargs.get('pro_version', None)

    # 主体部分
    res_dict = dict(
        # was_successful=True if test_results.wasSuccessful() else False,
        was_successful=test_results.wasSuccessful(),
        total=test_results.testsRun,
        failures=len(test_results.failures),
        errors=len(test_results.errors),
        skipped=len(test_results.skipped),
        run_time=run_time,
        pro_id=pro_id,
        pro_version=pro_version
    )

    # 详细信息部分
    failure_list = []  # 失败的内容
    for x in test_results.failures:
        note_data = {
            'test_case': x[0]._testMethodName,
            'explain': x[0]._testMethodDoc.rstrip('\n        :return:'),
            'status': 'failures',
            'note': x[1]
        }

        failure_list.append(note_data)

    for i in test_results.errors:
        note_data = {
            'test_case': i[0]._testMethodName,
            'explain': i[0]._testMethodDoc.rstrip('\n        :return:'),
            'status': 'errors',
            'note': i[1]
        }
        failure_list.append(note_data)

    res_dict['details'] = failure_list

    return res_dict


class TestReport(object):
    """
    测试报告自动化上传接口封装之后的类
    """

    def __init__(self):
        self.base_url = 'http://api.apiapp.cc'
        self.token = None
        self.appid = None
        self.appkey = None

    def set_base_url(self, base_url):
        """
        提供base_url的修改接口
        :param base_url:
        :return:
        """
        self.base_url = base_url

    def get_api_auth(self, **kwargs):
        """
        获取token
        :return:
        """

        appid = kwargs.get('appid', None)
        appkey = kwargs.get('appkey', None)

        if appid is None or appkey is None:
            return

        url = '%s/testdata/api-auth/' % self.base_url
        post_data = dict(
            appid_form=appid,
            appkey_form=appkey
        )

        res = requests.post(url, data=post_data)
        # print(res.text)
        res_json = json.loads(res.text)

        if res_json['code'] != 200:
            print('server api call exception~')
            return False

        self.token = res_json['data']['token']
        return True

    def post_unit_test_data(self, test_res_dict):
        """
        将接口测试结果给发送到服务器

        test_res_dict的格式必须如下所示:

        .. code::

            {
                "was_successful": false,
                "skipped": 7,
                "errors": 0,
                "failures": 10,
                "pro_id": "57a835c8c6e905166da11111",
                "total": 88,
                "run_time": 51.77724599838257,
                "details": [
                    {
                        "status": "failures",
                        "note": "AssertionError: 404 != 403 : gt不等于32位,返回404",
                        "explain": "gt不等于32位,返回404",
                        "test_case": "test_getfrontlib_gt_not32"
                    },
                    {...},
                    {...}
                ]
            }

        :param test_res_dict:
        :return:
        """
        # todo:做好字段检查

        url = '%s/testdata/create-test-data/?token=%s' % (self.base_url, self.token)

        res = requests.post(url, data=json.dumps(test_res_dict))
        # dlog.debug(res.text)

        # 做一个简单的检查
        res_dict = json.loads(res.text)
        assert res_dict['code'] == 200
