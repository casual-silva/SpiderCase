# -*- coding: utf-8 -*-

import io
import base64
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

url = 'http://www.python-spider.com/api/challenge13'

class GetSumValue():

    def __init__(self):
        self.number_list = []

    def get_page_data(self, page):
        rsp = requests.post(url, data={'page': page}, headers=headers)
        result = rsp.json()
        return result['woff'], result['data']

    def get_maps(self, extraNames):
        maps = {}
        # 解密映射逻辑
        for i, val in enumerate(extraNames):
            key = '&#x' + val[3:]
            _val = 0 if i == 9 else i + 1
            maps[key] = _val
        return maps

    def parse_woff(self, worf, page_num):
        worf_byte = base64.b64decode(worf)

        # 文件流编译成字体对象
        font = TTFont(io.BytesIO(worf_byte))
        font.saveXML(r'E:\SpiderCase\猿人云practice\css_font\13_css_font{}.xml'.format(page_num))
        # 解密映射逻辑
        extraNames = font.get('post').__dict__['extraNames']
        return extraNames

    def run(self, ):
        for page_num in range(1, 101):
            # 获取接口数据
            worf, data_list = self.get_page_data(page_num)
            # 解码
            extraNames = self.parse_woff(worf, page_num)
            # 加密css映射关系
            css_maps = self.get_maps(extraNames)
            # 遍历每一组分数
            for data in data_list:
                values = data['value'].split(' ')
                _number = [str(css_maps[val]) for val in values[:-1]]
                number = int(''.join(_number))
                self.number_list.append(number)
                print(number)
            break
        return sum(self.number_list)

if __name__ == '__main__':
    # sum_result = GetSumValue().run()
    # print(sum_result)
    pass
