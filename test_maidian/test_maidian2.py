import unittest, time, requests
from ddt import *

@ddt
class MyTestCase(unittest.TestCase):
    """ 数据埋点测试"""

    def setUp(self):
        self.url = "http://j10.dapi.uu.cc/yolanda"

    @data(('game_condition', 'avg_event_0015'), ('game_condition', 'avg_event_0033'),
          ('game_condition', 'avg_event_0049'), ('game_condition', 'avg_event_0052'),
          ('game_condition', 'avg_event_0053'), ('game_condition', 'avg_event_0054'),
          ('game_condition', 'avg_event_0055'), ('game_condition', 'avg_event_0056'),
          ('game_condition', 'avg_event_0057'), ('game_condition', 'avg_event_0058'),
          ('game_condition', 'avg_event_0059'), ('game_condition', 'avg_event_0060'),
          ('game_condition', 'avg_event_0061'), ('game_condition', 'avg_event_0062'),
          ('game_condition', 'avg_event_0064'),
          ('game_condition', 'avg_event_0065'), ('game_condition', 'avg_event_0066'),
          ('game_condition', 'avg_event_0067'), ('game_condition', 'avg_event_0068'),
          ('game_condition', 'avg_event_0069'), ('game_condition', 'avg_event_0070'),
          ('game_condition', 'avg_event_0071'), ('game_condition', 'avg_event_0072'),
          ('game_condition', 'avg_event_0073'), ('game_condition', 'avg_event_0074'),
          )
    @unpack
    def test_1(self, key, value):
        data = {
            'game_type': 'CustomEvent',
            'game_time': 2018111613,  #日期
            key: value,
            'request_id': 'e1eba4d4e19c11e8810c5254002f1a67'
                }
        res = requests.get(url=self.url, params=data, timeout=10)
        print(res.text)
        self.assertTrue(u"CustomEvent" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()


