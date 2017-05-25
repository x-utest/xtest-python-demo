import json

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



    def test_first_hello_world_true(self):
        """
        运行正确的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

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
