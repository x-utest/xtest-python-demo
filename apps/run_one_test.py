"""
运行单个测试函数，用于断点调试，不必运行所有的用例
"""
import unittest
from apps.account.units import AnoymousAccountApi, LoginAccountApi


def get_module_by_class(cls):
    return cls.__module__ + '.' + cls.__name__ + '.'


if __name__ == '__main__':
    test_fun = get_module_by_class(AnoymousAccountApi) + AnoymousAccountApi.test_user_logout.__name__
    print(test_fun)

    test_case_list = unittest.TestLoader().loadTestsFromName(test_fun)
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_case_list)  # 使用测试套件并打包测试用例

    test_result = unittest.TextTestRunner().run(test_suit)  # 运行测试套件，并返回测试结果
