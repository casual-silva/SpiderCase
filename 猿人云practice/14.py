
import requests
import execjs

headers = {
  # 'Host': 'www.python-spider.com',
  'Connection': 'keep-alive',
  'Content-Length': '7',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'http://www.python-spider.com',
  'Referer': 'http://www.python-spider.com/challenge/14',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'sessionid=j8elzq5pc68zz92p2vwgp9txsbh6by0u; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1607510465,1607585682,1607677977,1607926086; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1607941842'
}

api_url = 'http://www.python-spider.com/api/challenge14'
session = requests.Session()

value_list = []
def get_pages_data():
    ctx = js_func()
    for page in range(1, 101):
        uc = get_uc(ctx, page)
        json_data = fetch(page, uc)
        print(json_data)
        value_list.extend(json_data['data'])
    sum_data = sum((int(item['value']) for item in value_list))
    return sum_data

def js_func():
    with open('14.js', 'r') as fp:
        content = fp.read()
        ctx = execjs.compile(content)
        return ctx

def get_uc(ctx, page):
    uc = ctx.call('get_uc', page)
    return uc

def fetch(page, uc):
    resp = session.post(api_url, data={'page': page, 'uc': uc}, headers=headers)
    return resp.json()

if __name__ == '__main__':
    # sum_data = get_pages_data()
    # print(sum_data)
    pass

