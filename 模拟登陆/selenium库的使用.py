from selenium import webdriver
from lxml import etree
import requests
import os
from time import sleep
drive = webdriver.Chrome()
drive.set_window_size(1920,1080)
drive.get('https://cn.bing.com/?FORM=BEHPTB')
search_text = drive.find_element_by_xpath('//*[@id="sb_form_q"]')
search_text.send_keys('曹宜帆')
drive.find_element_by_xpath('//*[@id="sb_form_go"]').click()
drive.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
drive.close()
