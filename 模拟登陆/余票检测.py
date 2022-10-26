import requests
from time import sleep
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
url = 'https://kyfw.12306.cn/otn/leftTicket/query'
t = input('请输入出发时间(year-month-day):')
prarms = {
    'leftTicketDTO.train_date': t,
    'leftTicketDTO.from_station': 'ZZF',
    'leftTicketDTO.to_station': 'CDW',
    'purpose_codes': 'ADULT',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Cookie': 'JSESSIONID=FA4526338D3CEF97339991FA8635FF7C; BIGipServerotn=1022362122.38945.0000; BIGipServerpool_passport=384631306.50215.0000; RAIL_EXPIRATION=1593638054623; RAIL_DEVICEID=p2Bs5dgEnrcF41X-wDeigtnDXZv0AenGnEPl_cvgyt2x2Ul6In6dINtQQTJpsvB62pOUMy0y3PS6QRI0PC_vCuxOeZ3popfydL2MpkkkgePM4aBpZRRFNUEEkn6gXbhrQnHAJ0nOwqLgvEp8wW8qNWRRZpO7w6n4; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u90D1%u5DDE%2CZZF; _jc_save_fromDate=2020-06-28; _jc_save_toDate=2020-06-28; _jc_save_wfdc_flag=dc; _jc_save_toStation=%u6210%u90FD%2CCDW'
}
json_data_list = requests.get(url=url, headers=headers, params=prarms).json()['data']['result']
for str in json_data_list:
    print(str)






