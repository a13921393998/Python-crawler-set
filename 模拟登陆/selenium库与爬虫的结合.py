import selenium
from time import sleep
from lxml import etree
from selenium import webdriver
import time
import os
dirName = '企业名称'
url = 'http://125.35.6.84:81/xk/'
driver = webdriver.Chrome()
driver.get(url)
txt_name = dirName + '.txt'
f = open(txt_name,'w')
for i in range(7):
    start = time.time()
    if i != 1:
        driver.find_element_by_xpath('//*[@id="pageIto_next"]').click()
        sleep(2)
    driver.implicitly_wait(1)
    page_text = driver.page_source
    # driver.page_source方法返回的是实例化好的浏览器当前打开的页面源码数据
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        title = li.xpath('./dl/@title')[0]
        f.write(title+'\n')
driver.close()
f.close()
end = time.time()
use_time = end - start
print(use_time)



