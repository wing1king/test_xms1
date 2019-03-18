import unittest, time, requests
from ddt import *

@ddt
class MyTestCase(unittest.TestCase):
    """ 数据埋点测试"""

    def setUp(self):
        self.url = "http://j10.dapi.uu.cc/yolanda"

    @data(('game_condition', 'avg_event_0001'), ('game_condition', 'avg_event_0002'),
          ('game_condition', 'avg_event_0003'), ('game_condition', 'avg_event_0004'),
          ('game_condition', 'avg_event_0005'), ('game_condition', 'avg_event_0006'),
          ('game_condition', 'avg_event_0007'), ('game_condition', 'avg_event_0008'),
          ('game_condition', 'avg_event_0009'), ('game_condition', 'avg_event_0010'),
          ('game_condition', 'avg_event_0011'), ('game_condition', 'avg_event_0012'),
          ('game_condition', 'avg_event_0013'), ('game_condition', 'avg_event_0014'),
          ('game_condition', 'avg_event_0015'), ('game_condition', 'avg_event_0016'),
          ('game_condition', 'avg_event_0017'), ('game_condition', 'avg_event_0018'),
          ('game_condition', 'avg_event_0019'), ('game_condition', 'avg_event_0020'),
          ('game_condition', 'avg_event_0021'), ('game_condition', 'avg_event_0022'),
          ('game_condition', 'avg_event_0023'), ('game_condition', 'avg_event_0024'),
          ('game_condition', 'avg_event_0025'), ('game_condition', 'avg_event_0026'),
          ('game_condition', 'avg_event_0027'), ('game_condition', 'avg_event_0028'),
          ('game_condition', 'avg_event_0029'), ('game_condition', 'avg_event_0030'),
          ('game_condition', 'avg_event_0031'), ('game_condition', 'avg_event_0032'),
          ('game_condition', 'avg_event_0033'), ('game_condition', 'avg_event_0034'),
          ('game_condition', 'avg_event_0035'), ('game_condition', 'avg_event_0036'),
          ('game_condition', 'avg_event_0037'), ('game_condition', 'avg_event_0038'),
          ('game_condition', 'avg_event_0039'), ('game_condition', 'avg_event_0040'),
          ('game_condition', 'avg_event_0041'), ('game_condition', 'avg_event_0042'),
          ('game_condition', 'avg_event_0043'), ('game_condition', 'avg_event_0044'),
          )
    @unpack
    def test_1(self, key, value):
        data = {
            'game_type': 'CustomEvent',
            'game_time': 2018110616,  #日期
            key: value,
            'request_id': 'e1eba4d4e19c11e8810c5254002f1a67'
                }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"CustomEvent" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
