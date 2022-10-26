import requests
import os
from lxml import etree
dirName = 'pic'
if not os.path.exists(dirName):
    os.mkdir(dirName)
for i in range(1,2):
    if i == 1:
        url = 'http://pic.netbian.com/4kmeinv/index.html'
    else:
        url = 'http://pic.netbian.com/4kmeinv/' + 'index_' + str(i) + '.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    # 创建一个html的树的对象
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    # 属性定位,存储的是定位到的li标签
    for li in li_list:
        title = li.xpath('./a/img/@alt')[0] + '.jpg'
        pic_path = dirName + '/' + li.xpath('./a/img/@alt')[0] + '.jpg'
        # xpath返回标签属性，返回的是列表需要索引
        # 进行局部数据解析
        # 其中./表示的是li标签
        img_src = 'http://pic.netbian.com' +  li.xpath('./a/img/@src')[0]
        print(img_src)
        pic_response = requests.get(url=img_src,headers=headers).content
        f = open(pic_path,'wb')
        f.write(pic_response)
        f.close()
        print(title,'爬取成功')
