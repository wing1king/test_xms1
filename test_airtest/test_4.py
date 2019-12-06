import time, requests, unittest
from pprint import pprint
# Host = 'http://10.72.17.30'
url = 'http://119.29.1.133'


class MyTestCase(unittest.TestCase):


    def timestamp(str_time):
        time_list = str_time.split(":")
        return int(time_list[0]) * 60 * 60 + int(time_list[1]) * 60

    def _request(self):
        header = {
            "Content-Type": "text/plain",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImtpZC1oZWFkZXIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE1NzYyMzIyNjQsInVpZCI6MTExMTExMTExMTF9.c5KMcdUukKZ2UkMoiF9Fgbeissx9gY2QslYKk7lww0E"
        }
        data = {"room_id": 10000,
                "fields": ["play_schedule", "replay_times"],
                "room": {"play_schedule": 127,
                "replay_times": [{"start": self.timestamp("09:36"),"end": self.timestamp("09:38")}]}}
        resp = requests.post(url=url + "/app/voice/edit-room", json=data, headers=header)
        pprint(resp.text)

    def gain_user_gift(self):
        """加礼物"""
        header = {
            "Content-Type": "text/plain",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImtpZC1oZWFkZXIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE1NzYyMzIyNjQsInVpZCI6MTExMTExMTExMTF9.c5KMcdUukKZ2UkMoiF9Fgbeissx9gY2QslYKk7lww0E"
        }
        data = {
            "user_id": 99999999999,
            "gift_id": 1,
            "count": 10
        }
        res = requests.post(url=url + "/app/gift/gain-user-gift", headers=header, json=data)
        print(res.text)


def send_gift(self):
    """送礼物"""
    header = {
        "Content-Type": "text/plain",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImtpZC1oZWFkZXIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE1NzYyMzIyNjQsInVpZCI6MTExMTExMTExMTF9.c5KMcdUukKZ2UkMoiF9Fgbeissx9gY2QslYKk7lww0E"
    }
    data = {
        "user_id": 99999999999,
        "gift_id": 1,
        "count": 10,
        "item_id": 134073986386789,
        "item_type": 0,
        "room_id": 10000
    }
    res = requests.post(url=url + "/app/gift/send-gift", headers=header, json=data)
    print(res.text)


def tearDown(self):
    time.sleep(2)


if __name__ == "__main__":
    unittest.TestCase()
