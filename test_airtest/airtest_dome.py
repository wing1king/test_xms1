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

    def setUp(self):
        # 打开应用
        start_app("com.idreamsky.avg.platform")
        sleep(5)
        poco(name='android:id/button2').click()


    def test_1(self,test_info):
        pass

    def tearDown(self):
        # 回到桌面
        home()

    @classmethod
    def countTestCases(self):
        # 关闭应用
        stop_app("com.idreamsky.avg.platform")

if __name__ == '__main__':
    unittest.main()