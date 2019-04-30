import requests
import json
import threading
import time
import uuid


class postrequests():
    def __init__(self):
        self.url = 'http://10.72.12.44:112/v1/chat/id'

    def post(self):
        try:
            r = requests.post(self.url)
            print(r.text)
        except Exception as e:
            print(e)


def kquan_bf():
    login = postrequests()
    return login.post()


try:
    i = 0
    tasks_number = 10 # 开启线程数目
    print('测试启动')
    time1 = time.clock()
    while i < tasks_number:
        t = threading.Thread(target=kquan_bf)
        t.start()
        i += 1
    time2 = time.clock()
    times = time2 - time1
    print(times / tasks_number)
except Exception as e:
    print(e)
