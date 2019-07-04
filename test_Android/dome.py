from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'appPackage': 'io.dcloud.HBuilder',
                'appActivity': 'io.dcloud.PandoraEntryActivity',
                'deviceName':  'N8K5T16C26020898',
                'noReset': 'True'}
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

    def test_1(self):
        if self.driver.find_element_by_id('right_tv').click():  # 判断弹窗
            pass
        self.driver.find_element_by_class_name('android.widget.Image').click()
        sleep(1)

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
