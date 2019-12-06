import unittest
import requests
import time

url = "http://119.29.1.133"
user_id = 2366779543


def up_token():
    """生成token"""
    data = {
        "user_id": user_id  # 99999999999
            }
    res = requests.post(url=url + "/app/user/generate-token", json=data)
    return "Bearer " + res.json()["data"]["token"]


header = {
    "Content-Type": "text/plain",
    "Authorization": up_token()}


class MyTestCase(unittest.TestCase):
    """礼物"""

    def setUp(self):
        self.gift_id = 15743177594662   # 礼物ID
        self.count = 10000  # 房间ID

    def test_1(self):
        """加礼物"""
        data = {
            "user_id": user_id,
            "gift_id": self.gift_id,
            "count": self.count
        }
        res = requests.post(url=url + "/app/gift/gain-user-gift", headers=header, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_2(self):
        """送礼物"""
        data = {
            "user_id": user_id,    # 99999999999
            "gift_id": self.gift_id,
            "count": 1,     # 礼物数量
            "item_id": 134852586209280,  # 角色ID
            "item_type": 0,
            "room_id": self.count
        }
        res = requests.post(url=url + "/app/gift/send-gift", headers=header, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_3(self):
        """添加钻石"""
        data = {
            "user_id": user_id,    # 99999999999
            "value": 100,
            "currency_type": 0
        }
        res = requests.post(url=url + "/app/user/add-user-currency", headers=header, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_4(self):
        """发送房间聊天"""
        data = {
            "room_id": 135054911176704,    # 99999999999
            "content": "咕咕咕1",
            "nick_name": "好的好的"
        }
        res = requests.post(url=url + "/app/voice/send-chat", headers=header, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
