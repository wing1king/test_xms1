from time import *
import unittest
import warnings  # 忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'appPackage': 'com.idreamsky.avg.platform',
                'appActivity': 'com.idreamsky.activity.HomeActivity',
                'deviceName':  'N8K5T16C26020898',
                'noReset': 'True'}
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(11)
        cls.driver.find_element_by_id('item_personal_center').click()
        sleep(2)

    def test_a1(self):
        """点击头像进入个人主页点击历史和收藏"""
        self.driver.find_element_by_id('avatar__iv').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a1.jpg')
        sleep(1)
        self.driver.find_element_by_id('likes_tv').click()
        sleep(1)
        self.driver.find_element_by_id('lastest_visited_tv').click()
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a2(self):
        """签到"""
        self.driver.find_element_by_id('sign').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a2.jpg')
        sleep(1)
        self.driver.find_element_by_id('close_rl').click()
        sleep(2)

    def test_a3(self):
        """我的关注"""
        self.driver.find_element_by_id('view_following').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a3.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a4(self):
        """我的粉丝"""
        self.driver.find_element_by_id('view_fans').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a4.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a5(self):
        """星钻说明"""
        self.driver.find_element_by_id('diamond_rl').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a4.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a6(self):
        """星尘说明"""
        self.driver.find_element_by_id('key_rl').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a6.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a7(self):
        """进入充值中心"""
        self.driver.find_element_by_id('view_shop').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a7.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a8(self):
        """进入我的消息"""
        self.driver.find_element_by_id('view_news').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a8.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a9(self):
        """进入我的收藏"""
        self.driver.find_element_by_id('collections_rl').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a9.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a10(self):
        """进入浏览记录"""
        self.driver.find_element_by_id('history_rl').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a10.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a11(self):
        """进入个人信息"""
        self.driver.find_element_by_id('view_personalinformation').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a11.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a12(self):
        """进入客服反馈"""
        self.driver.find_element_by_id('view_customservice').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a12.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    def test_a13(self):
        """进入系统设置"""
        self.driver.find_element_by_id('setting').click()
        sleep(1)
        self.driver.save_screenshot('E:/App_jietu/a13.jpg')
        sleep(1)
        self.driver.find_element_by_id('back_rl').click()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
