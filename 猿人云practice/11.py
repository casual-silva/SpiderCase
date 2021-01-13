import re
import execjs
import requests

headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Referer': 'http://www.python-spider.com/challenge/11',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
}

cookies = {
    'sessionid': 'a6qth7mmti2nayj0jmdyyed96snnip7g',
}

pre_js_attach = '''
document = {
    'attachEvent': attachEvent,
    'createElement': createElement,
};
function createElement(a, b) {
    return {
        'innerHTML': 'http://www.python-spider.com/challenge/11',
        'firstChild': {'href': 'http://www.python-spider.com/challenge/11'}
    }

};
location = {
    'href': '',
    'search': '',
    'pathname': '',

};
function setTimeout(a,b) {
};
function attachEvent(a, b) {
    document[a] = b;
};
'''

alf_js_attach = '''
function get_cookie(){
    _N();
    return document.cookie
};
'''

url = 'http://www.python-spider.com/challenge/11'


def fetch():
    resp = requests.get(url, headers=headers, cookies=cookies)
    if '<script>' == resp.text[:8]:
        jsl_jscode = re.findall('<script>(.*?)</script>', resp.text, re.S)[0]
        return jsl_jscode
    return resp.text

def main():
    # 解析加速乐代码
    _jsl_jscode = fetch()
    jsl_jscode = pre_js_attach + _jsl_jscode + alf_js_attach
    ctx = execjs.compile(jsl_jscode)
    _cookie = ctx.call('get_cookie')
    __jsl_clearance = _cookie.split('=')[1]
    cookies['__jsl_clearance'] = __jsl_clearance

    # 获取cookie完毕
    print(cookies)
    result_text = fetch()
    numbers = re.findall('<td class="info">[\s]+(\d+)[\s]+</td>', result_text, re.S)
    print(numbers)
    result = sum((int(num) for num in numbers))
    return result

if __name__ == '__main__':
    print(main())
