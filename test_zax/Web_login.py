#coding:utf-8
import unittest
from selenium import webdriver
from time import sleep


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.maximize_window()

    def login(self, username, password):
        self.dr.get('https://dev.report.ellearn.cn/oms/#/login')
        self.dr.find_element_by_name('username').send_keys(username)
        self.dr.find_element_by_name('password').send_keys(password)
        self.dr.find_element_by_xpath("/html/body/div/div/div/form/div/div[2]/div[3]/div/button").click()

    def test_1(self):
        """账号密码正确"""
        self.login("admin5", "123456")
        sleep(3)
        link = self.dr.find_element_by_id('app')
        self.assertTrue(u'' in link.text)
        self.dr.get_screenshot_as_file(r"E:\jietu\1.png")

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()

# #coding=UTF-8
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("testing")
# driver.find_element_by_id("su").click()
# driver.quit()

