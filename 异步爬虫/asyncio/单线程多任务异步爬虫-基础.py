import requests
import asyncio
import time


# 回调函数的封装
def task_callback(t):
    print('I am a task_callback(),参数t：', t)
    # 参数t：该函数的调用者，此处是任务对象task
    print('t.result()返回值：', t.result())
    # result()方法返回的是特殊函数的返回值


async def get_requets(url):
    # 一个函数被async修饰后，则该函数就变成了一个特殊函数
    # 特殊之处有两个
    # 1.该函数被调用后不会立刻执行
    # 2.该函数被调用后会返回一个携程对象
    print('正在请求的url：',url)
    time.sleep(2)
    print('请求结束：',url)
    return 'bobo'


# 创建一个携程对象
c = get_requets('www.baidu.com')


# asyncio.ensure_futre()创建一个任务对象
task = asyncio.ensure_future(c)
# 其中参数为一个被async修饰过的函数对象



# 任务对象task绑定回调函数
task.add_done_callback(task_callback)
# 执行完任务后，才会执行回调函数
# 回调函数只能有一个参数，这个参数在回调中，传入的是任务对象task


# 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 将任务对象注册到事件循环中且开启事件循环
loop.run_until_complete(task)












