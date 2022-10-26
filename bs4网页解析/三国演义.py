import requests
from bs4 import BeautifulSoup
import os
dirName = 'romance of the three kingdoms'
if not os.path.exists(dirName):
    os.mkdir(dirName)
url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
page_text = requests.get(url=url,headers=headers)
response = page_text.text
soup = BeautifulSoup(response,'lxml')
# 创建一个BeautifulSoup对象，对网页数据进行lxml解析
a_list = soup.select('.book-mulu > ul > li > a')
for a in a_list:
    title = a.string
    txt_name = dirName + '/' + title + '.txt'
    text_url = 'http://www.shicimingju.com' + a['href']
    page_text_detail = requests.get(url=text_url,headers=headers)
    response_txt = page_text_detail.text
    soup_new = BeautifulSoup(response_txt,'lxml')
    div_tag = soup_new.find('div',class_='chapter_content')
    content = div_tag.text
    f = open(txt_name,'w',encoding='utf-8')
    f.write(content)
    f.close()
    print(title,'爬取成功')
