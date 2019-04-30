#coding:utf-8
from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver
from ddt import *

@ddt
class MyTestCase(unittest.TestCase):
    global test_info
    test_info = []
    for i in range(10):  # 执行次数
        tese_data = (i, i + 1)
        test_info.append(tese_data)
    @classmethod
    def setUp(self):
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'appPackage': 'com.idreamsky.avg.platform',
                'appActivity': 'com.idreamsky.activity.HomeActivity',
                'deviceName':  'N8K5T16C26020898',
                'noReset': 'True'}
            # {
            #     'platformName': 'Android',
            #     'platformVersion': '6.0',
            #     # 'appPackage': 'com.idreamsky.avg.platform',
            #     # 'appActivity': 'com.idreamsky.activity.HomeActivity',
            #     'app': 'D:\\hyhd-1_v1.0.0_s2.1.0_BG0S0N00001-vivo.apk',
            #     'deviceName': '127.0.0.1:7555',
            #     'noReset': 'True'}
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    @data(*test_info)
    def test_1(self, test_info):
        self.driver.tap([(300, 782)])
        sleep(0.5)
        self.driver.tap([(500, 782)])
        sleep(0.5)
        self.driver.tap([(700, 782)])
        sleep(0.5)
        self.driver.tap([(900, 782)])
        sleep(0.5)
        self.driver.tap([(100, 782)])

    @classmethod
    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()

# import uiautomator2 as u1
# from time import sleep
# d = u1.connect('192.168.1.128')
#
# # 启动App
# d.app_start("d://com.idreamsky.avg.platform_1.0.0_3.apk")
#
# # 搜索
# d(resourceId="com.meizu.mzbbs:id/j0").click()
#
# # 输入关键字
# d(resourceId="com.meizu.mzbbs:id/p9").set_text("flyme")
#
# # 搜索按钮
# d(resourceId="com.meizu.mzbbs:id/tp").click()
#
# sleep(2)
#
# # 停止app
# d.app_stop("com.meizu.mzbbs")