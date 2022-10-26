import requests
from lxml import etree
import os
from bs4 import BeautifulSoup
url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
response = requests.get(url=url,headers=headers)
page_text = response.text
tree = etree.HTML(page_text)
# hot_cities = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
# print(hot_cities)
# all_cities = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
# print(all_cities)
cities = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div[2]/li/a/text()')
# | 管道符的作用是管道符左右两侧的xpath可以同时生效，如果只有一个可以生效，则生效一个
print(cities)
