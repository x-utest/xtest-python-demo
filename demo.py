"""
Python演示,上传数据
- python > 3.5

参考 wiki：

.. code::

    http://api.apiapp.cc/static/wiki/index.html

"""

import time
import unittest

from xtest_sdk import TestReport, dict_encode_test_results

# todo 在系统中注册了,组织信息中看到这个值,替换到此处
project_id = '590c2a0947fc894a51f9e616'  # 项目的编号值
app_id = '3832f354872411e6a7c700163e006b26'
app_key = '38342936872411e6a7c700163e006b26'


class MyTestDemo(unittest.TestCase):
    """
    pyunit使用示例
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_first_hello_world_true(self):
        """
        运行正确的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

    def test_first_hello_world_true2(self):
        """
        运行正确的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

    def test_first_hello_world_false(self):
        """这里面的文档会在报告里面
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    def test_first_hello_world_false2(self):
        """用户登录不正常
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    def test_first_hello_world_false(self):
        """用户不应该越权访问资源
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    def test_first_hello_world_false2(self):
        """此处用户操作太多内容了
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    def test_first_hello_world_false3(self):
        """这个用户不是超级管理员
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    def test_first_hello_world_false4(self):
        """此处删除数据后不应该还能查询得到
        :return:
        """
        self.assertTrue(True, msg='Hello Word是失败的')


if __name__ == '__main__':
    # 使用Pyunit框架可以构建一个如下的测试结果字典,然后上传到服务器即可

    start_time = time.time()  # 测试启动的时刻点

    test_cases = unittest.TestLoader().loadTestsFromTestCase(MyTestDemo)  # 装载测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)  # 使用测试套件并打包测试用例

    test_result = unittest.TextTestRunner().run(test_suit)  # 运行测试套件，并返回测试结果

    total_time = time.time() - start_time  # 测试过程整体的耗时

    test_res_dict = dict_encode_test_results(
        test_result,
        run_time=total_time,
        pro_id=project_id,
        pro_version='2.17.5.5.1'  # 当前被测试的系统的版本号,依据目前系统的信息
    )

    # 下面的内容是将测试报告的结果上传到服务器
    test_report = TestReport()
    auth_res = test_report.get_api_auth(app_id=app_id, app_key=app_key)
    if auth_res:
        test_report.post_unit_test_data(test_res_dict)
    else:
        print('auth error...')
