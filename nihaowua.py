import requests
import random
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_random_ua(): #随机UA
	ua = UserAgent()
	return ua.random

headers = {
    'User-Agent': get_random_ua()
}

url = 'https://www.nihaowua.com/'

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

def get_proxies(): #随机IP
    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    return proxies

def main_print(): #直接打印输出程序
    count = 0
    while True:
        res = requests.get(url=url, headers=headers, proxies=get_proxies())
        res.encoding = 'utf-8'
        selector = etree.HTML(res.text)
        xpath_reg = "//section/div/*/text()"
        results = selector.xpath(xpath_reg)
        content = results[0]
        count += 1
        print('********正在爬取中，这是第{}次爬取********'.format(count))
        print(content)

def main_keep(): #写入txt文本程序
    count = 0
    with open("NiHaoWu.txt", "a") as f:
            while True:
                res = requests.get(url=url, headers=headers, proxies=get_proxies())
                res.encoding = 'utf-8'
                selector = etree.HTML(res.text)
                xpath_reg = "//section/div/*/text()"
                results = selector.xpath(xpath_reg)
                content = results[0]
                f.write(content + '\n')
                count += 1
                print('********正在爬取中，这是第{}次爬取********'.format(count))

if __name__ == '__main__':
        main_print()