#!/usr/bin/python
# -*- coding: UTF-8 -*
import execjs
import requests

headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1607500840,1607510465; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1607511774',
  'Host': 'www.python-spider.com',
  'Pragma': 'no-cache',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://www.python-spider.com/challenge/1',
  'safe': '185cb1570ab35920b5a0e8dbe3d5604d',
  'timestamp': '1607566873',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}


def get_safe_val():
    with open('1.js') as fp:
        js_code = fp.read()
        cxt = execjs.compile(js_code)
        safe = cxt.call('get_sage_token')
        return safe

count = 0
api_url = 'http://www.python-spider.com/challenge/api/json?page={}&count=14'
def get_pages_data():
    for page in range(1, 86):
        api_page_url = api_url.format(page)
        result = fetch(api_page_url)
        global count
        for info in result['infos']:
            if '招' in info['message']:
                count += 1
                print(info['message'])
    return count

def fetch(url):
    timestamp, safe = get_safe_val()
    headers['safe'] = safe
    headers['timestamp'] =timestamp
    resp = requests.get(url, headers=headers)
    result = resp.json()
    if not result.get('infos'):
        raise Exception
    return result


if __name__ == '__main__':
    count = get_pages_data()
    print(count)
