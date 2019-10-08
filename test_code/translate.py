# -*- coding:utf-8 -*-
import requests


def translate2(string):
    """
    translate by youdao.com
    :param string: a str waiting for translate.
    :return: a str translated form 'string'
    """
    # string = str(input("请输入一段要翻译的文字："))
    data = {
        'doctype': 'json',
        'type': 'AUTO',
        'i': string
    }
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url, params=data)
    result = r.json()['translateResult'][0][0]['tgt']
    print(result)
    return result
