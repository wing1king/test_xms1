from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """句子页面点击播放后进入配音页面—循环"""
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'appPackage': 'com.idreamsky.avg.platform',
                'appActivity': 'com.idreamsky.activity.HomeActivity',
                'deviceName':  'N8K5T16C26020898',
                'noReset': 'True'}
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def test_1(self):
        self.driver.find_element_by_id('item_my_game').click()
        sleep(1)
        count = 0
        while count < 5:
            self.driver.find_element_by_id('iv_play').click()
            sleep(8)
            self.driver.find_element_by_id('img_listen_me').click()
            sleep(5)
            self.driver.find_element_by_class_name('android.widget.ImageView').click()
            sleep(1)
            count += 1

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
