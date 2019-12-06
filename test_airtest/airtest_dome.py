import unittest, time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 连接设备
        connect_device("Android:N8K5T16C26020898")
        sleep(2)
        start_app("com.idreamsky.riko")

    def test_1(self):
        count = 0
        poco(text="剧场").click()
        sleep(2)
        touch([513, 1211])
        sleep(2)
        #while True:
        while count < 100:
            sleep(0.1)
            touch([980, 1707])
            print('点击')
            count += 1


    def tearDown(self):
        # 回到桌面
        home()
        sleep(2)

    @classmethod
    def countTestCases(self):
        # 关闭应用
        stop_app("com.idreamsky.avg.platform")

if __name__ == '__main__':
    unittest.main()