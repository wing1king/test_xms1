from airtest.core.api import *
import unittest


class WSTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 连接设备
        connect_device("android:///N8K5T16C26020898")

    def setUp(self):
        # 启动App
        start_app("com.idreamsky.avg.platform")
        sleep(5)

    def test_1(self):
        # 滑动屏幕
        # for fouce_i in range(5):
        #     swipe(v1=(950, 850), v2=(300, 850))
        #     sleep(1)
        touch((500, 500), times=1)
        sleep(5)
        # 点击屏幕
        touch((500, 1700), times=10000000, duration=1)

    def tearDown(self):
        # 返回桌面
        home()

    @classmethod
    def tearDownClass(cls):
        # 结束App
        stop_app("com.idreamsky.avg.platform")