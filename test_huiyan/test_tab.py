from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
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
        count = 0
        while True:
            self.driver.tap([(300, 782)])
            sleep(0.1)
            self.driver.tap([(500, 782)])
            sleep(0.1)
            self.driver.tap([(700, 782)])
            sleep(0.1)
            self.driver.tap([(900, 782)])
            sleep(0.1)
            self.driver.tap([(100, 782)])
            count += 1

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
