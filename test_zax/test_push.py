import unittest
import requests


class MyTestCase(unittest.TestCase):
    """"""

    def setUp(self):
        self.url = "https://openapi.xg.qq.com/v3/push/app"
        self.headers = {
                        'Authorization': "Basic MGQ3ZjI5Yjg4OTE2YzpkNWU3MzQwNjE3OTJmZDQwNzJkZDU2ODZmYWFjMDg0Mw==",
                        'Content-Type': "application/json",
                        'Postman-Token': "17e54bab-fa03-48ea-aac7-1c284a93b8d5,36a19d46-7686-4bfb-b6d4-15b94b184f87",
                        'cache-control': "no-cache,no-cache"}
        self.payload = {
                    "platform": "ios",
                    "environment": "dev",
                    "audience_type": "all",
                    "message_type": "notify",
                    "message": {"ios": {"aps": {"alert": "milo 21"}}}}

    def test_1(self):
        res = requests.post(url=self.url, headers=self.headers, data=self.payload)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
