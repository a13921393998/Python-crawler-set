import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
for page in range(1,9):
    print("page:"+str(page))
    data = {
        'cname': '',
        'pid': '',
        'keyword': '上海',
        'pageIndex': str(page),
        'pageSize': '10'
        }
    response = requests.post(url=url,headers=headers,data=data)
    # data参数是post方法中处理参数动态化的参数
    page_text = response.json()
    for dic in page_text['Table1']:
        storeName = dic['storeName']
        addressDetail = dic['addressDetail']
        print(storeName," "*10,addressDetail)
