
import requests
import execjs

headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  # 'Cache-Control': 'no-cache',
  # 'Connection': 'keep-alive',
  # 'Content-Length': '6',
  # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'sessionid=tp0ngw5n3sehu1iuwlqfc6rm2gipfw33',
  # 'Host': 'www.python-spider.com',
  # 'Origin': 'http://www.python-spider.com',
  # 'Pragma': 'no-cache',
  # 'Referer': 'http://www.python-spider.com/challenge/16',
  'safe': 'MTYwODA5ODQ4OQ==|AAAACAAAAAgAAAAEAAAAAAAAAAIAAAAAAAAAAAAAAAQAAAAIAAAABgAAAAAAAAAAAAAAAwAAAAEAAAAAAAAACAAAAAAAAAAIAAAAAAAAAAEAAAAFAAAAAAAAAAMAAAAAAAAAAwAAAAIAAAAAAAAACAAAAAMAAAAIAAAABAAAAAIAAAAGAAAABgAAAAUAAAAAAAAAAQAAAAAAAAAAAAAAAQ8+o2Pi7Yr3zoq0nQwfBj4HEvaBw',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
  # 'X-Requested-With': 'XMLHttpRequest'
}

api_url = 'http://www.python-spider.com/api/challenge16'

value_list = []
def get_pages_data():
    ctx = js_func()
    for page in range(1, 101):
        token = get_token(ctx)
        json_data = fetch(page, token)
        value_list.extend(json_data['data'])
    sum_data = sum((int(item['value']) for item in value_list))
    return sum_data

def js_func():
    with open('16.js', 'r') as fp:
        content = fp.read()
        ctx = execjs.compile(content)
        return ctx

def get_token(ctx):
    token = ctx.call('get_token')
    return token

def fetch(page, token):
    print(token)
    headers['safe'] = token
    resp = requests.post(api_url, data={'page': page}, headers=headers)
    print(resp.text)
    return resp.json()

if __name__ == '__main__':
    sum_data = get_pages_data()
    print(sum_data)
