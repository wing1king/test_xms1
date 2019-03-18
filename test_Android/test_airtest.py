from airtest.core.api import *
import unittest


class WSTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect_device("android:///N8K5T16C26020898")

    def setUp(self):
        # 启动App
        start_app("com.idreamsky.avg.platform")
        sleep(5)

    def test_1(self):
        # 滑动屏幕
        swipe(v1=(950, 850), v2=(300, 850))
        sleep(1)
        swipe(v1=(950, 850), v2=(300, 850))
        sleep(1)
        swipe(v1=(950, 850), v2=(300, 850))
        sleep(1)
        # 点击封面
        touch((500, 500), times=1)
        sleep(5)
        # 点击屏幕
        touch((500, 1700), times=10000000, duration=0.5)

    def tearDown(self):
        home()

    @classmethod
    def tearDownClass(cls):
        stop_app("com.idreamsky.avg.platform")