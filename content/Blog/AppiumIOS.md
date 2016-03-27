Title:Appium在iOS端实现的脚本片段。
Date:2015-05-13
Category:Blog
Tags:Appium,iOS
Summary:Appium在iOS端实现的脚本片段，记录备份。


    # coding:utf-8
    from appium import webdriver
    import time
    import os
    import time
    
    success = True
    desired_caps = {}
    desired_caps['appium-version'] = '1.0'
    desired_caps['platformName'] = 'iOS'
    desired_caps['autoLaunch'] = 'true'
    desired_caps['platformVersion'] = '8.1.2'
    desired_caps['deviceName'] = 'TestIphone6'
    desired_caps['bundleId'] = 'io.appium.TestApp'
    desired_caps['udid'] = 'd67350bd7dc62308dea8e919803441128cb11745'
    
    wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    wd.implicitly_wait(10)
    
    def is_alert_present(wd):
        try:
            wd.switch_to_alert().text
            return True
        except:
            return False
    
    try:
        wd.find_element_by_name("TextField1").send_keys("1")
        wd.find_element_by_name("IntegerB").send_keys("2")
        wd.find_element_by_name("ComputeSumButton").click()
        time.sleep(5)
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")