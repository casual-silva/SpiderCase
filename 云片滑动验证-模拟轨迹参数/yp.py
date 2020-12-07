import time
import json
import execjs
import random
import requests


class EncryptCollision:

    def __init__(self):
        self.headers = {
            'Referer': 'https://www.yunpian.com/product-captcha.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }
        self.ctx = self.reload_js()
        self.traces = list(self.read_traces())

    def read_traces(self):
        with open('trace.txt', 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()

    def reload_js(self):
        """
        加载 js
        :return:
        """
        with open('yp.js', 'rb') as f:
            js = f.read().decode()
        ctx = execjs.compile(js)
        return ctx

    def get_cb(self, ctx):
        """
        生成 cb 参数
        :param ctx:
        :return:
        """
        return ctx.call('get_cb')

    def generate_trace(self, ctx, distance):
        """
        生成轨迹
        :param ctx:
        :param distance:
        :return:
        """
        return ctx.call('get_trace', distance)

    def encrypt_data(self, ctx, data):
        """
        js 加密, 生成 i, k 参数, 其中 i 参数为 AES 加密, k 参数为 RSA 加密
        :param ctx:
        :param data:
        :return:
        """
        return ctx.call('encrypt', data)

    def init_slider(self, ctx):
        """
        初始化验证码
        :return:
        """
        url = 'https://captcha.yunpian.com/v1/jsonp/captcha/get'

        # 浏览器环境等参数, 可固定
        data = {
            "browserInfo": [
                {"key": "userAgent",
                 "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"},
                {"key": "language", "value": "zh-CN"},
                {"key": "hardware_concurrency", "value": 4},
                {"key": "resolution", "value": [1366, 768]},
                {"key": "navigator_platform", "value": "Win32"}
            ],
            "mobile": "",
            "nativeInfo": {},
            "options": {
                "sdk": "https://www.yunpian.com/static/official/js/libs/riddler-sdk-0.2.2.js?version=d64b4905b3d97729a01f89b39459c6ae"},
            "fp": "87a6ecfe812d030a3c2885223270da33",
            "address": "https://www.yunpian.com",
            "yp_riddler_id": "0dd345b7-b3b5-4c48-8b33-93dd4970e11f"
        }

        encrypt_data = self.encrypt_data(ctx, data)
        params = {
            'cb': self.get_cb(ctx),
            'i': encrypt_data['i'],
            'k': encrypt_data['k'],
            'captchaId': '974cd565f11545b6a5006d10dc324281'  # 固定值
        }
        resp = requests.get(url, params=params, headers=self.headers)
        result = json.loads(resp.text.replace('ypjsonp(', '').replace(')', ''))
        if result['msg'] == 'ok':
            bg = result['data']['bg']
            fg = result['data']['front']
            token = result['data']['token']
            return {
                'captcha_url': bg,
                'slider_url': fg,
                'token': token
            }
        return None

    def collision(self):
        """
        滑块碰撞
        :return:
        """
        url = 'https://captcha.yunpian.com/v1/jsonp/captcha/verify'

        while True:
            init_data = self.init_slider(self.ctx)
            if init_data:
                break
        distance = 95  # 滑动距离
        trace = self.generate_trace(self.ctx, distance)
        data = {
            'points': trace,
            'distanceX': 0.2903225806451613,
            'fp': "87a6ecfe812d030a3c2885223270da33",  # 指纹可固定
            'address': "https://www.yunpian.com",
            'yp_riddler_id': "0dd345b7-b3b5-4c48-8b33-93dd4970e11f"  # 这个不知道啥也可以固定
        }

        encrypt_data = self.ctx.call('encrypt', data)
        params = {
            'cb': self.ctx.call('get_cb'),
            'i': encrypt_data['i'],
            'k': encrypt_data['k'],
            'token': init_data['token'],
            'captchaId': '974cd565f11545b6a5006d10dc324281'
        }
        # 验证参数
        resp = requests.get(url, headers=self.headers, params=params)
        result = json.loads(resp.text.replace('ypjsonp(', '').replace(')', ''))
        print(result)
        if result['msg'] == 'ok':
            print({
                'success': 1,
                'message': '校验成功! ',
                'data': data,
                'distance': distance
            })
            self.save_trace(data)  # 保存成功的轨迹

    def collision_verify(self):
        """
        滑块碰撞验证
        :return:
        """
        url = 'https://captcha.yunpian.com/v1/jsonp/captcha/verify'

        while True:
            init_data = self.init_slider(self.ctx)
            if init_data:
                break
        data = json.loads(random.choice(self.traces))
        encrypt_data = self.ctx.call('encrypt', data)
        params = {
            'cb': self.ctx.call('get_cb'),
            'i': encrypt_data['i'],
            'k': encrypt_data['k'],
            'token': init_data['token'],
            'captchaId': '974cd565f11545b6a5006d10dc324281'
        }
        # 验证参数
        resp = requests.get(url, headers=self.headers, params=params)
        result = json.loads(resp.text.replace('ypjsonp(', '').replace(')', ''))
        print(result)
        if result['msg'] == 'ok':
            print({
                'success': 1,
                'message': '校验成功! ',
                'data': data,
            })

    def save_trace(self, trace):
        with open('trace.txt', 'a', encoding='utf-8') as fp:
            fp.write(json.dumps(trace) + '\n')


if __name__ == '__main__':
    encryptCollision = EncryptCollision()
    while True:
        try:
            # result = encryptCollision.collision()
            result = encryptCollision.collision_verify()
        except Exception as e:
            print('验证失败！', e)
