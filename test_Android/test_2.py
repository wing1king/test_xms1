#coding:utf-8
from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):
    """"""
    def setUp(self):
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '6.0',
                # 'appPackage': 'com.idreamsky.avg.platform',
                # 'appActivity': 'com.idreamsky.activity.HomeActivity',
                'app': 'D:\\hyhd-1_v1.0.0_s2.1.0_BG0S0N00001-vivo.apk',
                'deviceName': '127.0.0.1:7555',
                'noReset': 'True'}
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def test_1(self):
        # try:
        #     self.driver.find_element_by_id("button2").click()
        # except ZeroDivisionError:
        #     print("未弹出")
        # self.driver.swipe(760, 600, 200, 600)  # 向左滑动
        self.driver.find_element_by_id("game_img").click()
        sleep(2)
        # self.driver.find_element_by_id("img_button_download").click()
        # sleep(5)
        elems = self.driver.find_element_by_class_name("android.view.View")
        while True:
            sleep(1)
            elems.click()
            try:
                print("正常点击")
            except Exception as e:
                print(e)
                print("异常")

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