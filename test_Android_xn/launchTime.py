import csv
import os
import time


class App(object):
    """App启动时间"""
    def __init__(self):
        self.content = ""
        self.startTime = 0

    def LaunchApp(self):
        """启动App"""
        cmd = 'adb shell am start -W -n com.idreamsky.avg.platform/com.idreamsky.activity.LaunchActivity'
        self.content = os.popen(cmd)
        time.sleep(5)

    def StopApp(self):
        """停止App"""
        #  结束App
        #cmd = 'adb shell am force-stop com.idreamsky.avg.platform'
        #  推到后台
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)
        time.sleep(5)

    def GetLaunchedTime(self):
        """获取启动时间"""
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


class Controller(object):
    """控制类"""
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp", "elapsedtime")]

    def testprocess(self):
        """单次测试过程"""
        self.app.LaunchApp()
        elpasedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, elpasedtime))

    def run(self):
        """多次执行测试过程"""
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    def getCurrentTime(self):
        """获取当前的时间戳"""
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    def SaveDataToCSV(self):
        """数据的存储"""
        tinecsv = 'time.csv'
        csvfile = open(tinecsv, 'w')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    """执行次数"""
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()