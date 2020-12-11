

import requests




api_url = 'http://www.python-spider.com/api/challenge6'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '7',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'sessionid=sg14ocwf8qhj999gxi4rado6qy4dpkkl;',
    'Host': 'www.python-spider.com',
    'Origin': 'http://www.python-spider.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.python-spider.com/challenge/6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

session = requests.session()
session.headers.update(headers)

value_list = []
def get_pages_data():
    for page in range(1, 101):
        json_data = fetch(page)
        print(json_data)

        value_list.extend(json_data['data'])
    sum_data = sum((int(item['value']) for item in value_list))
    return sum_data

def fetch(page):
    params = {
        "page": page
    }
    resp = session.post(api_url, data=params)
    print(resp.headers, resp.cookies)
    if session.cookies.get_dict():
        session.cookies.update(session.cookies.get_dict())
    return resp.json()

if __name__ == '__main__':
    sum_data = get_pages_data()
    print(sum_data)