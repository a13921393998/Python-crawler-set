import requests
import time
from time import sleep
from lxml import etree
from selenium.webdriver import ActionChains
from selenium import webdriver
# 引入动作链相关的库

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver = webdriver.Chrome()
driver.get(url)
action = ActionChains(driver)
# 实例化一个动作链对象，将动作链和实例化好的浏览器对象进行绑定
driver.implicitly_wait(1)
driver.switch_to.frame('iframeResult')
# driver.switch_to.frame将页面定位到指定的嵌套页面中，该方法的参数为嵌套页面的id
div_tag = driver.find_element_by_xpath('//*[@id="draggable"]')
# 如果使用driver.find_element_by_xpath寻找的标签在iframe中是无法定位的
# iframe标签指的是页面嵌套
# 解决方法使用switch_to
action.click_and_hold(div_tag)
# action.click_and_hold()表示点击且查看
for i in range(6):
    action.move_by_offset(10,15).perform()
    # 根据指定的像素移动
    # .perform()方法表示动作链立刻执行
    sleep(0.5)
    # action.move_to_element('//*[@id="droppable"]')
    # 直接移动到我们指定的标签
driver.close()



