import requests
import random
from lxml import etree
from fake_useragent import UserAgent

def get_random_ua(): #随机UA
    ua = UserAgent()
    return ua.random

headers = {
    'User-Agent': get_random_ua()
}

url = 'https://www.nihaowua.com/home.html'

def main(): #写入txt文本程序
    count = 0
    with open("soup.txt", "a") as f:
            while True:
                res = requests.get(url=url, headers=headers,timeout=10)
                res.encoding = 'utf-8'
                selector = etree.HTML(res.text)
                xpath_reg = "//section/div/*/text()"
                results = selector.xpath(xpath_reg)
                content = results[0]
                f.write(content + '\n')
                count += 1
                print('********正在爬取中，这是第{}次爬取********'.format(count))

if __name__ == '__main__':
	main()