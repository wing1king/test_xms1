#coding:utf-8
from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):
    """首页"""
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'appPackage': 'com.idreamsky.avg.platform',
            'appActivity': 'com.idreamsky.activity.LaunchActivity',
            'deviceName': '127.0.0.1:7555',
            'unicodeKeyboard': 'True',
            'restKeyboard': 'True',
            'noReset': 'True'
                    }
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

    def test_1(self):
        """作品点赞"""
        self.driver.find_element_by_id("like_count").click()
        sleep(2)
        self.driver.get_screenshot_as_file(r"D:souye_1.png")

    def test_2(self):
        """进入作品详情"""
        self.driver.find_element_by_id('content_tv').click()
        sleep(2)
        self.driver.get_screenshot_as_file(r'souye_2.png')

    def tearDown(self):
        self.driver.quit()
        sleep(5)


if __name__ == '__main__':
    unittest.main()
