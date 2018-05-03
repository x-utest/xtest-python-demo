# coding:utf-8

"""
封装的sdk
"""
import json
import requests

from dtlib import jsontool
from dtlib.dtlog import dlog


class WebApiSdk(object):
    def __init__(self):
        self.base_url = ''
        self.appid = ''
        self.appkey = ''
        self.token = ''

    def init_cfg(self, **kwargs):

        base_url = kwargs.get('base_url', None)
        appid = kwargs.get('appid', None)
        appkey = kwargs.get('appkey', None)

        assert base_url is not None
        assert appid is not None
        assert appkey is not None

        self.base_url = base_url
        self.appid = appid
        self.appkey = appkey

    def wrap_token(self, params):
        """
        将请求参数中代入token
        :param params:
        :return:
        """
        params.update(token=self.token)
        return params

    def warp_url_token(self, url):
        """
        对url包装一层token
        :param url:
        :return:
        """
        url = '%s?token=%s' % (url, self.token)
        return url

    def get_auth_token(self):
        """
        进行接口认证,获取token,不再使用session的方式了
        :return:
        """
        auth_url = '%s/testdata/api-auth/' % self.base_url
        auth_data = {
            'appid_form': self.appid,
            'appkey_form': self.appkey
        }

        res = requests.post(auth_url, data=auth_data)
        res_json = json.loads(res.text)
        token = res_json['data']['token']
        dlog.debug(token)
        self.token = token

    def get_font_version(self):
        """
        获取前段参数版本号
        :return:
        """
        url = '%s/gtcap/get-front-version-list/' % self.base_url

        params = self.wrap_token(params=dict())
        res = requests.get(url, params=params)
        return res.text

    # def send_exec_server_api_tests_callback(self, **kwargs):
    #     """
    #     执行脚本完毕后，发送的回调方法
    #     :return:
    #     """
    #     url = "%s/gtcap/callback-exec-server-api-tests/" % self.base_url
    #
    #     # params = dict(
    #     #     success
    #     # )
    #
    #     res = requests.get(url)
    #     dlog.debug(res.text)
    #     res_dict = json.loads(res.text)
    #     return res_dict

    def create_ab_data(self, data):
        """
        ab测试数据
        :param data:
        :return:
        """
        url = '%s/testdata/create-perform-report/' % self.base_url
        res = requests.post(url, data)
        return res.text

    def create_apiserver_testdata(self, data):
        if len(data) == 7:
            url = '%s/testdata/create-apiserver-testdata/' % self.base_url
        else:
            url = '%s/testdata/create-apiserver-testdata-note/' % self.base_url

        data = self.wrap_token(data)
        res = requests.post(url, data)
        return res.text

    def create_unit_test_data(self, data):
        """
        单元测试的数据
        :param data:
        :return:
        """
        url = '%s/testdata/create-test-data/' % self.base_url
        # data = self.wrap_token(data)
        url = self.warp_url_token(url)
        res = requests.post(url, jsontool.dumps(data))
        return res.text

    def send_feedback_msg(self, **kwargs):
        """
        调用反馈的接口-微信发消息
        :param kwargs:
        :return:
        """
        url = kwargs.get('url', 'http://gt-jenkins.geetest.com')
        nickname = kwargs.get('nickname', '反馈消息')
        content = kwargs.get('content', '持续集成')
        remark = kwargs.get('remark', '完成一次构建')

        feedback_msg_url = '%s/wechat/send-feedback-tpl-msg/' % self.base_url

        post_param = dict(
            url=url,
            nickname=nickname,
            content=content,
            remark=remark,
            token=self.token
        )

        res = requests.post(
            feedback_msg_url,
            data=post_param
        )
        dlog.debug(res.text)


if __name__ == '__main__':
    sdk = WebApiSdk()
    # sdk.base_url = 'http://sshdev2.ft42.com'
    sdk.base_url = 'http://192.168.1.200:8009'
    sdk.get_auth_token()
    sdk.send_feedback_msg()
    # sdk.send_exec_server_api_tests_callback()


    # webapisdk = WebApiSdk()
    # webapisdk.base_url = 'http://sshdev.geetest.com'
    # webapisdk.get_auth_session()
    # res = webapisdk.get_font_version()
