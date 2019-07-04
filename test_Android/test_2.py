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
        if self.driver.find_element_by_id('button2').click():  # 判断弹窗
            pass
        self.driver.swipe(950, 850, 500, 850)
        sleep(1)
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        sleep(2)
        self.driver.find_element_by_id("bt_start_game").click()
        sleep(2)
        if self.driver.find_element_by_id('right_tv').click():  # 判断弹窗
            pass
        # try:
        #     self.driver.find_element_by_id('right_tv').click()
        # except:
        #     print("未弹出")
        self.driver.find_element_by_id("img_button_play").click()
        sleep(10)
        elems = self.driver.find_element_by_class_name("android.view.View")
        while True:
            sleep(0.5)
            elems.click()
            try:
                print("正常点击")
            except Exception as e:
                print(e)
                print("点击错误")

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
