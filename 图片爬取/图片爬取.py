import requests
url = 'https://tse3-mm.cn.bing.net/th/id/OIP.td_DIYRJm2f3XpLCrbHhKQHaFk?pid=Api&rs=1'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
params = {
    'pid': 'Api',
    'rs': '1'
    }
response = requests.get(url=url,headers=headers,params=params)
img = response.content
# content返回的是二进制形式的数据
with open('img.jpg','wb') as fp:
    # wb模式以二进制方式写入数据
    fp.write(img)
print('爬取成功')
