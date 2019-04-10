import requests
import json
import threading
import time
import uuid


class postrequests():
    def __init__(self):
        # 产生UUID
        #         u = uuid.uuid1()
        #         # 产生订单编号
        orderID = 'TEST' + u.hex
        self.url = 'http://10.72.12.44:112/v1/chat/id'
        self.data = {"payOrderNo": orderID, "userId": "16500", "activityId": "1103",
                     "couponIdNumMap": {"2580": 2, "2581": 2, "2582": 2}}
        self.headers = {'content-type': 'application/json'}
        self.data = json.dumps(self.data)

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
    tasks_number = 1000 # 开启线程数目
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
