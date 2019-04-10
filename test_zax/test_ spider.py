from bs4 import BeautifulSoup
import requests, sys, urllib3, time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""
注意：
1.urllib3 为忽略异常提示
2.verify=False  为忽略ssl认证
3.html5lib  为解决报错
4.timeout=60000 为解决超时
"""


class downloader(object):

    def __init__(self):
        self.server = "http://www.biqukan.com/"
        self.target = "http://www.biqukan.com/1_1094/"
        self.names = []
        self.urls = []
        self.nums = []

    def get_download_url(self):
        res = requests.get(url=self.target, verify=False, timeout=60000)
        html = res.text
        div_bf = BeautifulSoup(html, 'html5lib')
        div = div_bf.find_all('div', class_='listmain' )
        a_bf = BeautifulSoup(str(div[0]), 'html5lib')
        a = a_bf.find_all('a')
        self.nums = len(a[15:1314])
        for each in a[15:1314]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target, verify=False, timeout=60000)
        html = req.text
        bf = BeautifulSoup(html, 'html5lib')
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一念永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], r'D:\\一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一念永恒》下载完成')
