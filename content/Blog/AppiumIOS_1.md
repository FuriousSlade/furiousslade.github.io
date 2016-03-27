Title:基于Appium实现IOS自动化测试。
Date:2015-06-29 17:30
Category:Blog
Tags:Python,Appium
Summary:简述使用Appium实现iOS自动化测试的过程。

## Appium的安装

要实现ios自动化前提是有一台Mac OS X操作系统的设备可以是正统的mac或是黑苹果。然后去<a href='http://appium.io' target='_blank'>appium官网</a>下载appium服务端。osx上不推荐使用命令行安装，因为命令行看装会缺失appium inspector这个重要的元素定位工具。建议使用dmg安装包安装appium。然后在安装相应的appium client，我用的是python。`pip install appium-python-client`来完成client的安装。

## iOS演示Demo的创建

先安装**xcode**。因为没有开发者证书所以只能用ios模拟器来演示，在这里不多说了。从<a href="https://github.com/appium/sample-code" target="_blank">https://github.com/appium/sample-code</a>上下载appium的演示DEMO。

1. 下载后进入```sample-code/apps/TestApp```目录下
2. 执行```xcodebuild -sdk iphonesimulator```来编译所需的TestApp。
3. 看到```BUILD SUCCEEDED```TestApp就编译成功了。
4. 在```sample-code-master/sample-code/apps/TestApp/build/release-iphonesimulator```目录下可以看到TestApp.app就是后面所需要使用的app。


## Appium的配置

启动appium,点击**苹果**图标。
![](http://ww2.sinaimg.cn/large/0067jSM2gw1etlbot0j3fj31100wemzq.jpg)
点击”Choose”,选择之前编译生成的TestApp.app。并选择模拟设备”iPhone6"，系统版本为”8.3”。最后再次点击苹果图标确认设置。
![](http://ww1.sinaimg.cn/large/0067jSM2gw1etlbp3wwuxj31280wejyc.jpg)
点击放大镜按钮，来启动appium inspector控件元素识别工具。
![](http://ww2.sinaimg.cn/large/0067jSM2gw1etlbpgwfv0j31100we4fs.jpg)
此时inspector工具和iOS模拟器会同时启动。使用inspector可以很方便的查看控件的各类属性。
![](http://ww1.sinaimg.cn/large/0067jSM2gw1etlbpp9n9mj31kw0xldmw.jpg)

## 测试代码

``` python
# coding=utf8
import pytest
import sys
from appium import webdriver
import random

class TestClass(object):

    '''初始化weddriver链接'''
    @classmethod
    def setup_class(self):
        desired_caps = {}
        # appium版本
        desired_caps['appium-version'] = '1.4.1'
        # 平台为iOS
        desired_caps['platformName'] = 'iOS'
        # 自启动被测应用
        desired_caps['autoLaunch'] = 'true'
        # iOS系统版本
        desired_caps['platformVersion'] = '8.3' 
        # 设备为iPhone模拟器
        desired_caps['deviceName'] = 'iPhone Simulator'
        # 需要上传至iPhone模拟器的被测应用
        desired_caps[
            'app'] = "/Users/slade/Downloads/sample-code-master/sample-code/apps/TestApp/build/release-iphonesimulator/TestApp.app"
        # 创建webdriver链接
        self.wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(30) # 等待元素出现时间为30秒

    '''验证TestApp求和功能'''

    def test_one(self):
        text_one = random.randint(1, 100)   # 创建1-100随机数
        text_two = random.randint(1, 100)   # 创建1-100随机数
        # 对第一个输入框输入第一个随机数
        self.wd.find_element_by_name("TextField1").send_keys(text_one)
        # 对第二个输入框输入第二个随机数
        self.wd.find_element_by_name("IntegerB").send_keys(text_two)
        # 点击求和按钮
        self.wd.find_element_by_name("ComputeSumButton").click()
        # 确定TestApp的求和计算结果
        answer = self.wd.find_element_by_name("Answer").text
        # 断言TestApp求和功能是否正确
        assert int(answer) == text_one + text_two

    '''释放webdriver链接'''
    @classmethod
    def teardown_class(self):
        self.wd.quit()

if __name__ == '__main__':
    # 使用了单元测试框架pytest作为驱动
    pytest.main(sys.argv[0] + ' -s')
```


## 执行

![](http://ww1.sinaimg.cn/large/0067jSM2gw1etn2ma2khtg30hs0b4u0y.gif)