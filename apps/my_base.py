"""
弄一个最基础的类，然后方便后续统一修改和扩展
"""
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
