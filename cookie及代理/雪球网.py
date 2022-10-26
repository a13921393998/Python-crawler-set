import requests
from lxml import etree
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Cookie': 'aliyungf_tc=AQAAALg+en3ZrQ0APgDRtw28gzaQZEgG\
; xq_a_token=ea139be840cf88ff8c30e6943cf26aba8ad77358\
; xqat=ea139be840cf88ff8c30e6943cf26aba8ad77358\
; xq_r_token=863970f9d67d944596be27965d13c6929b5264fe\
; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9\
.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5NDAwMjgwOCwiY3RtIjoxNTkyNDU5NjA2MjQ5LCJjaWQiOiJkOWQwbjRBWnVwIn0\
.eD5rPlaT6oU0EMpDAVOFfXtcKOnF__GZ2ilkdnwudhU95JiXOXSOHkO-66bz9uuITLFfCoQI6c2JEBmJdETaWWdhRRbT6BOEsYUBToF7j\
_YdVYAwdQ-q_OVgkawjMQueWlE-JZ9t7saPFbPKnzry4pLfvUAoabShyIFurD6UXatBJFM3xz9DuuFqRDgZiibxbgMC8-7cc2yWDdfS912XrJhPgrvj\
xnd7w9QqSYI64XkXv0MDiR9XMHbgbKGcjA45SgsI0b7GNL_9ekDSIA-QayDnKWFIRa8bObyRqNN7-HvOGx8e93TTIg5xsg8oah6R32MHFkIMYBCmbc6618Lafg\
; u=951592459652934; device_id=24700f9f1986800ab4fcc880530dd0ed\
; acw_tc=2760820b15924614546664576e8401fdf32e2202fd821270d455e539a99518\
; Hm_lvt_1db88642e346389874251b5a1eded6e3=1592461804,1592461806,1592462020,1592462130\
; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1592462130'
    }
main_url = 'https://xueqiu.com/'
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=66103&size=15'
session.get(main_url,headers=headers)
page_text = requests.get(url=url,headers=headers).json()
print(page_text)


