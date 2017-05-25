
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

# 运行环境

- python3.5


# 文件介绍


- `./xtest/sdk.py`
    对接口进行的封装和一些工具函数，使用的库文件
- `demo.py`
    接口的调用demo



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

# 发布公告


## 1.17.5.25.1

- 第二版的demo
- 以项目组织的多文件
- 开始准备写大型的测试项目了


## 1.16.10.21.1

- 第一版的demo
- 单个文件的test项目