# -*- coding: utf-8 -*-
import requests
from fontTools.ttLib import TTFont

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
    'Cookie': 'sessionid=vr6fic7bhulsfqwn9k1d54pdi4v0g8cw',
}

def save_xml():
        font = TTFont('12.woff')
        font.saveXML(r'12_css_font.xml')
        extraNames = font.get('post').__dict__['extraNames']
        return extraNames

def get_css_maps():
    extraNames = save_xml()
    # 匹配映射规则
    maps = {}
    for key, val in enumerate(extraNames):
        if key == 9:
            num = 0
        else:
            num = key + 1
        v = '&#x' + val[3:]
        maps[v] = num
    return maps



url = 'http://www.python-spider.com/api/challenge12'
def fetch(page):
    resp = requests.post(url, data={'page': page}, headers=headers)
    return resp.json()

def main():
    # 获取字体加密映射
    css_maps = get_css_maps()
    # 获取所有数据
    number_list = []
    for page in range(1, 101):
        datas = fetch(page)
        for data in datas['data']:
            values = data['value'].split(' ')
            _number = [str(css_maps[val]) for val in values[:-1]]
            number = int(''.join(_number))
            number_list.append(number)
            print(number)
    return sum(number_list)

if __name__ == '__main__':
    sum_result = main()
    print(sum_result)