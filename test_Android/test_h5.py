import time
import unittest
import warnings
from appium import webdriver


class MyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'deviceName': 'N8K5T16C26020898',
            'unicodeKeyboard': 'True',
            'restKeyboard': 'True',
            'noReset': 'True'
                        }
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(8)
        cls.driver.find_element_by_id('b6e').click()
        time.sleep(2)
        cls.driver.find_element_by_id('apn').click()
        time.sleep(5)

    def test_home_page(self):
        """"""
        # self.driver.tap([(860, 1230)])  # 重新开始
        self.driver.tap([(850, 1430)])  # 继续阅读
        elems = self.driver.find_element_by_class_name('android.widget.FrameLayout')
        while True:
            time.sleep(0.5)
            elems.click()
            try:
                print("正常点击")
            except Exception as e:
                print(e)
                print("点击错误")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



