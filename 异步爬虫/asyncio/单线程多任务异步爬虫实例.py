import requests
import asyncio
import time
'''
注意事项:
在特殊函数内部不可以出现不支持异步模块对应的代码，否则会中断异步效果
'''

async def get_requets(url):
    # 一个函数被async修饰后，则该函数就变成了一个特殊函数
    # 特殊之处有两个
    # 1.该函数被调用后不会立刻执行
    # 2.该函数被调用后会返回一个携程对象
    print('正在请求的url：',url)
    await asyncio.sleep(2)
    # 出现了不支持异步模块的代码
    # 异步代码会跳过阻塞代码，所以这里必须加一个await关键字
    # await关键字的作用：在特殊函数内部，凡是阻塞操作前都必须使用await进行修饰，await可以保证在异步执行过程中不会被跳过

    print('请求结束：',url)
    return 'bobo'


urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.4399.com'
]
start = time.time()
tasks = []

if __name__ == '__main__':
    for url in urls:
        c = get_requets(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    # 创建时间循环对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    # 循环对象绑定任务对象时，参数只能是一个任务对象，而不能是一个列表
    # 通过asyncio.wait()方法对tasks列表进行封装
    # asyncio.wait()方法赋予列表中的任务对象，可挂起的权限。只有任务对象被赋予了可被挂起的权限后，该任务对象才可以被挂起。
    # 挂起：将当前任务交出cpu的使用权
    end = time.time()
    use_time = end - start
    print('消耗时间:', use_time)










