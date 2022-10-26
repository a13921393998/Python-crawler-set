import requests
url = 'https://movie.douban.com/j/search_subjects'
params = {
    'type': 'movie',
    'tag': '动作',
    'sort': 'recommend',
    'page_limit': '20',
    'page_start': '0'
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
response = requests.get(url=url,headers=headers,params=params)
response.encoding = 'utf-8'
page_text = response.text
# page_text = response.json()
# 将获取的字符串形式的json数据序列化成字典或者列表 
# for movie in page_text:
    # name = movie['title']
    # score = movie['score']
    # print(name,score)
    # 将列表中我们需要的数据拿出来
    # 带上cookie才能运行该代码


with open('douban.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
print('douban.html','爬取成功')
