import re
import time
import execjs
import requests

js_str = '''
document = {};
location = {};
window = {
    'm': function b(a) {
    },
    'k': function a(a) {
    },
    'navigator': {
        'webdriver': '',
    },
};

function setInterval(a, b) {

};

function get_sign() {
    return document
};

'''

headers = {
 "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
 "Accept-Encoding": "gzip, deflate",
 "Accept-Language": "zh-CN,zh;q=0.9",
 "Cache-Control": "no-cache",
 "Cookie": "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1608274353,1609154236,1609923849,1610348413; sessionid=bimz56melgmj4x3xomm0fe2tbp50k5y9; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1610350570",
 "Host": "www.python-spider.com",
 "Pragma": "no-cache",
 "Proxy-Connection": "keep-alive",
 "Referer": "http",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
 "X-Requested-With": "XMLHttpRequest"
}

api_city_url = 'http://www.python-spider.com/cityjson'
api_arstjs_url = 'http://www.python-spider.com/api/challenge15/js?_t={0}&_={1}'
api_data_url = 'http://www.python-spider.com/api/challenge15'

data_list = []

def get_arstjs():
    # 请求预先接口
    print('request:', api_city_url)
    resp = requests.get(api_city_url, headers=headers, timeout=10)
    time_str = re.findall('"timestamp": "(\d+)"}', resp.text)[0]

    # 请求真实arst混淆接口
    _api_arstjs = api_arstjs_url.format(time_str, int(time.time() * 1000))
    print('get:', _api_arstjs)
    resp = requests.get(_api_arstjs, headers=headers, timeout=10)
    arst_text = resp.text
    return arst_text

def js_func(arst_text):
    jscode = js_str + arst_text
    ctx = execjs.compile(jscode)
    cookie = ctx.call('get_sign')
    sign = re.findall('sign=(.*?);', str(cookie))[0]
    return sign

def get_sign():
    try:
        arst_text = get_arstjs()
        sign = js_func(arst_text)
        return sign
    except:
        return get_sign()

def get_data(page):
    sign = get_sign()
    print('get_page >>', page)
    resp = requests.get(api_data_url, json={"page": str(page), "sign": sign}, headers=headers)
    result = resp.json()
    data_list.extend([int(item['value']) for item in result['data']])

def run():
    for page in range(1,101):
        get_data(page)
    print(data_list)
    return sum(data_list)

if __name__ == '__main__':
    print(run())
