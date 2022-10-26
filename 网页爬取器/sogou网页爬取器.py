import requests
KeyWord = input("enter a key word:")
# 携带了请求参数的url，如果想要爬取不同关键字对应的页面，我们需要将url进行动态化
# 实现参数动态化
params = {
    'query':KeyWord
    }
# params参数（字典）：保存请求时url携带的参数
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
# UA反爬机制破解


url = 'https://www.sogou.com/web?'
# ?可加可不加
response = requests.get(url=url,params=params,headers=headers)
response.encoding = 'utf-8'
# 将获取的数据编码格式进行更改
page_text = response.text
fileName = KeyWord + '.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName,'爬取成功')
