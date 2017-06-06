import json
from unittest import skip

import requests

from apps.my_base import MyBaseTest, domain


class MyTestDemo(MyBaseTest):
    """
    pyunit使用示例
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @skip('just demo')
    def test_first_hello_world_true(self):
        """
        运行正确的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

    @skip('just demo')
    def test_first_hello_world_true(self):
        """
        运行正确的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

    @skip('just demo')
    def test_first_hello_world_true2(self):
        """
        运行正确的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

    @skip('just demo')
    def test_first_hello_world_false(self):
        """这里面的文档会在报告里面
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    @skip('just demo')
    def test_first_hello_world_false2(self):
        """用户登录不正常
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    @skip('just demo')
    def test_first_hello_world_false3(self):
        """这个用户不是超级管理员
        :return:
        """
        self.assertTrue(False, msg='Hello Word是失败的')

    @skip('just demo')
    def test_first_hello_world_false4(self):
        """此处删除数据后不应该还能查询得到
        :return:
        """
        self.assertTrue(True, msg='Hello Word是失败的')
