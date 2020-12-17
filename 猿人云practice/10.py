
import requests

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
  'Referer': 'http://www.python-spider.com/challenge/10',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  # 'Cookie': 'sessionid=sg14ocwf8qhj999gxi4rado6qy4dpkkl; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1607500840,1607510465,1607585682; __jsl_clearance=1607591603.890|0|clD4VpfqhdaLBWywKWy%2FZyfi6d_09a956b67b3ee1fa9db414b490d0f0bc3D; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1607591605; sign=1607580112~YWlkaW5nX3dpbjM5L*'
}

api_url = 'http://www.python-spider.com/api/challenge10'
value_list = []
session = requests.Session()
def get_pages_data():
    for page in range(1, 101):
        json_data = fetch(page)
        print(json_data)
        value_list.extend(json_data['data'])
    sum_data = sum((int(item['value']) for item in value_list))
    return sum_data


def fetch(page):
    session.headers.clear()
    session.headers.update(headers)
    resp = session.post(api_url, data={'page': page})
    return resp.json()

if __name__ == '__main__':
    sum_data = get_pages_data()
    print(sum_data)