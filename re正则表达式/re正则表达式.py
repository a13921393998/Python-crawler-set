import requests
import re
import os
dirName =  'pic'
if not os.path.exists(dirName):
    os.mkdir(dirName)
i = 0
for s in range(85,109):
    url = 'http://www.521609.com/daxuemeinv/list' + str(s) + '.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }
    response = requests.get(url=url,headers=headers)
    page_text = response.text
    Xpath = '<li>.*?<img src="(.*?)".*?</li>'
    img_herf = re.findall(Xpath,page_text,re.S)
    for src in img_herf:
        src = 'http://www.521609.com' + src
        response_pic = requests.get(url=src,headers=headers)
        pic = response_pic.content
        i = i + 1
        pic_name = dirName + '/' + str(i) + '.jpg'
        with open(pic_name,'wb') as f:
            f.write(pic)
            f.close()
        print(src,'爬取成功')
