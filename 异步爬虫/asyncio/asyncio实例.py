# import requests
import time
import asyncio
import aiohttp
from lxml import etree
# requests 库不支持异步爬虫
# aiohttp 库用于异步爬虫

urls = [
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/cao',
    'http://127.0.0.1:5000/bobo'
]


'''
aiohttp 库的使用
    1.先打框架：
        async def get_requests(url):
            # 实例化对象，放在关闭实例化对象出错，使用with...as语法
            with aiohttp.ClientSession() as sess:
                # 将请求数据保存到response中，为防止关闭实例化对象出错，使用with...as语法
                with sess.get(url=url) as response:
                    # sess.get/post(url=url,headers=headers,params/data=params/data,proxy=='http://ip:port')
                    # proxy是一个代理ip的参数
                    # 获取了字符串形式是数据
                    page_text = response.text
                    lenth = len(page_text)
                    return lenth
    2.补充细节：
        在阻塞的前面加await关键字
        在with前加async关键字
    3.完整代码：获取字符串.text();获取byte类型的数据，使用.read()
        async def get_requests(url):
            # 实例化对象，放在关闭实例化对象出错，使用with...as语法
            async with aiohttp.ClientSession() as sess:
                # 将请求数据保存到response中，为防止关闭实例化对象出错，使用with...as语法
                async with await sess.get(url=url) as response:
                    # sess.get/post(url=url,headers=headers,params/data=params/data,proxy=='http://ip:port')
                    # proxy是一个代理ip的参数
                    # 获取了字符串形式是数据
                    page_text = await response.text()
                    return page_text
    4.多任务爬虫数据的解析，必须使用回调函数
    
'''

test_url = []
def task_callback(t):
    # result()方法返回的是特殊函数的返回值
    # t为任务对象task而任务对象封装了一个特殊函数
    page_text = t.result()
    tree = etree.HTML(page_text)
    trs = tree.xpath('//*[@id="category_150"]/table//tr')
    # xpath解析不运行出现tbody标签，应该跳过
    for tr in trs:
        tds = tr.xpath('./td[@class="fl_g"]')
        for td in tds:
            url = 'https://www.bigpar.com/' + td.xpath('./div/a/@href')[0]
            test_url.append(url)
    print(test_url)

async def get_requests(url):
    # 实例化对象，放在关闭实例化对象出错，使用with...as语法
    async with aiohttp.ClientSession() as sess:
        # 将请求数据保存到response中，为防止关闭实例化对象出错，使用with...as语法
        async with await sess.get(url=url) as response:
            # sess.get/post(url=url,headers=headers,params/data=params/data,proxy=='http://ip:port')
            # proxy是一个代理ip的参数
            # 获取了字符串形式是数据
            page_text = await response.text()
            return page_text

start = time.time()
tasks = []
for url in urls:
    c = get_requests(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
    # 任务对象task绑定回调函数
    task.add_done_callback(task_callback)
    # 执行完任务后，才会执行回调函数
    # 回调函数只能有一个参数，这个参数在回调中，传入的是任务对象task
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
use_time = end - start
print('总耗时:', use_time)













