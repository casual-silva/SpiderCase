# -*- coding: utf-8 -*-

import io
import json
import base64
import js2py
import requests
from fontTools.ttLib import TTFont

jscode = '''function getnames(){
    window = {}
    name_list = [];
    let name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];
    let data = [{"value": "&#xe798 &#xe285 &#xe798 &#xf693 "}, {"value": "&#xc471 &#xa468 &#xf817 &#xb195 "}, {"value": "&#xe798 &#xa641 &#xc471 &#xb938 "}, {"value": "&#xb938 &#xc471 &#xc471 &#xa468 "}, {"value": "&#xc249 &#xa468 &#xe798 &#xc249 "}, {"value": "&#xb938 &#xb938 &#xa641 &#xb938 "}, {"value": "&#xe285 &#xb195 &#xa641 &#xa468 "}, {"value": "&#xb938 &#xf817 &#xa468 &#xa468 "}, {"value": "&#xf817 &#xc471 &#xa468 &#xa468 "}, {"value": "&#xc249 &#xf817 &#xc249 &#xb938 "}];
    i = 0;
    for (i; i<5; i++){
        window.page = i + 1;
        j = 0;
        let yyq = 1;
        page_names = [];
        for (j; j < data.length; j++){
            page_names.push(name[yyq + (window.page - 1) * 10]);
            yyq += 1;
        };
        name_list.push(page_names)
    };
    return name_list;
}'''

class GetBestMan():

    def __init__(self):
        self.code_number_list = []

    def run(self, ):
        for page_num in range(1, 6):
            number_list = []
            url = 'http://match.yuanrenxue.com/api/match/7?page={}'.format(page_num)
            worf, data_list = self.get_page_data(url)

            # 解码
            worf_byte = base64.b64decode(worf)

            # 文件流编译成字体对象
            font = TTFont(io.BytesIO(worf_byte))

            # 解密映射逻辑
            extraNames = font.get('post').__dict__['extraNames']
            maps = self.get_maps(extraNames)

            # 遍历每一组分数
            for v in data_list:
                num = ''
                values = v['value'].split(' ')[:-1]
                for val in values:
                    value = val[3:]
                    num += str(maps[value])
                number_list.append(int(num))
            self.code_number_list.append(number_list)
            #  存储便于检查分析
            font.saveXML(r'css_font{}.xml'.format(page_num))

        # 所有加密映射数据解析完毕
        result = self.return_best_name(self.code_number_list)
        print('最强男人：', result)
        return result

    def get_name_list(self, ):
        return js2py.eval_js(jscode)()

    def get_page_data(self, url):
        rsp = requests.get(url)
        result = json.loads(rsp.content)
        return result['woff'], result['data']

    def return_best_name(self, code_number_list):
        # 最大分数对应的名字
        _name_list = []
        name_list = self.get_name_list()
        name_list = [_name_list.extend(item) for item in name_list]

        _code_number_list = []
        code_number_list = [_code_number_list.extend(item) for item in code_number_list]

        print('所有玩家数据：', dict(zip(_name_list, _code_number_list)))
        return _name_list[_code_number_list.index(max(_code_number_list))]

    def get_maps(self, extraNames):
        maps = {}
        # 解密映射逻辑
        for i, val in enumerate(extraNames):
            key = val[3:]
            _val = 0 if i == 9 else i + 1
            maps[key] = _val
        return maps


if __name__ == '__main__':
    GetBestMan().run()
