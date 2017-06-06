"""
弄一个最基础的类，然后方便后续统一修改和扩展
"""
import json
import unittest

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

    def assertStatusOk(self, res):
        """
        先保证服务接口是可用的最基本检测
        :param res:
        :return:
        """
        status_code = res.status_code
        self.assertEqual(status_code, 200, msg='服务需要能正常响应')

    def assertResCodeOk(self, res_text):
        """
        服务能完成正常的通讯流程
        :param res_text:
        :return:
        """
        code = json.loads(res_text).get('code', None)
        self.assertEqual(code, 200, msg='业务接口需要能按照设定的模板返回值')

    def assertResCodeForbidden(self, res_text):
        """
        服务能完成正常的通讯流程
        :param res_text:
        :return:
        """
        code = json.loads(res_text).get('code', None)
        self.assertEqual(code, 403, msg='业务接口返回值为禁止')


class MyLoginBaseTest(MyBaseTest):
    def __init__(self, *args, **kwargs):
        """
        一些参数设置
        """
        super(MyLoginBaseTest, self).__init__(*args, **kwargs)

        self.path = '%s/account' % domain
        # todo 通过任意的方式进行登录，然后获取到token,替换到此处
        self.token = 'ce4900384a8611e7939200163e006b26815f445e'
        # url = self.path + '/user-login/'
        #
        # post_data = dict(
        #     user='test_user',
        #     password='asdf1234',
        # )
        #
        # res = requests.post(url, data=json.dumps(post_data))
        #
        # # print(res.text)
        #
        # res_json = json.loads(res.text)
        # self.token = res_json['data']['token']

    def wrap_param_with_token(self, param_dict):
        """
        在参数后面包装在token
        :param url:
        :return:
        """
        param_dict['token'] = self.token
        return param_dict

    def setUp(self):
        pass

    def tearDown(self):
        pass
