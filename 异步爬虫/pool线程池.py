import requests
import time
from multiprocessing.dummy import Pool
def get_rqeuest(url):
    page_text = requests.get(url=url).text
    return len(page_text)

# 同步代码
# start = time.time()
urls = [
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/cao',
    'http://127.0.0.1:5000/bobo'
]
# for url in urls:
    # res = get_rqeuest(url)
    # print(res)
# end = time.time()
# use_time = end - start
# print('总耗时:', use_time)


# 异步代码
start = time.time()
pool = Pool(3)
# 表示开启线程的数量
result_list = pool.map(get_rqeuest, urls)
# 第一个参数为func参数为一个回调函数，第二个参数为alist是回调函数的参数列表
# 其中回调函数必须有一个返回值和参数
print(result_list)
end = time.time()
use_time = end - start
print('总耗时:', use_time)



