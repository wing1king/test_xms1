import unittest, time, requests
from ddt import data,ddt


@ddt
class MyTestCase(unittest.TestCase):
    global test_info
    test_info = []
    for i in range(10): # 执行次数
        tese_data = (i, i + 1)
        test_info.append(tese_data)

    def setUp(self):
        pass

    @data(*test_info)
    def test_1(self,test_info):
        res = requests.post(url="http://10.72.12.44:112/v1/chat/id")
        datas = open("1.txt", 'w')
        for i in range(10):
            print(res.json()['data'], file=datas)



if __name__ == '__main__':
    unittest.main()