
# 基本介绍


一个完整的,自动化测试过程:

1. 编写自动化代码
2. 运行自动化代码
1. 提取测试结果
1. 上传测试结果
1. 图表化展示结果


在使用本程序之前，请先在 [xtest](http://xtest.apiapp.cc) 系统中注册，
```
http://xtest.apiapp.cc
```

并获取具体项目的配置信息：

- app_id
- app_key
- pro_id

修改本项目中的 `./apps/xtest_cfg.py` 中的配置参数

# 运行环境

- python3.5


# 文件介绍


- `./xtest/sdk.py`
    对接口进行的封装和一些工具函数，使用的库文件
- `apps`
    接口测试的项目

    - start.py 测试项目运行
    - xtest_cfg 测试项目线上报告系统配置



# 说明


接口的使用规范。


# 使用方法

```
cd xtest-python-demo
./install.sh
```

这样 xtest 的sdk就安装成功了。


运行起示例的方法：

1. 将 `app_id`,`app_key`,`pro_id`替换成自己在系统中注册的账号提供的内容
1. 直接运行此文件

```
cd xtest-python-demo
python apps/start.py
```

然后就可以在 xtest 系统中看到图表了：

![](xtest-share-report.png)


# 友情链接


[使用文本文件写自动化测试用例](https://github.com/TesterlifeRaymond/doraemon)：

```
https://github.com/TesterlifeRaymond/doraemon
```

一个用来模拟服务器端返回请求的[测试平台](http://git.oschina.net/pinghailinfeng/nbmock)，也可以用于档板测试


```
http://git.oschina.net/pinghailinfeng/nbmock
```


# 项目实战

为了让本项目有更实际的意义，所以决定将 xtest 这个系统的接口自动化测试给开源出来，大家可以一起看和点评，同时可以一起来写。

一直苦于没有接口自动化项目实战经验的朋友，欢迎加入和讨论。

如果有兴趣一起交流的的朋友，可以加入：

    互联网软件测试开发QQ群： `207548681`


# 发布公告


## 1.17.5.25.1

- 第二版的demo
- 以项目组织的多文件
- 开始准备写大型的测试项目了
- 加入了对版本信息的api的测试用例


## 1.16.10.21.1

- 第一版的demo
- 单个文件的test项目