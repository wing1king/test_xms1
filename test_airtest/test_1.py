import unittest, time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:N8K5T16C26020898")
sleep(5)
start_app("com.idreamsky.avg.platform")
sleep(5)
poco(name='android:id/button2').click()
home()
sleep(5)
stop_app("com.idreamsky.avg.platform")
sleep(5)
