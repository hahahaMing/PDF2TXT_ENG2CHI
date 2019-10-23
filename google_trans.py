from googletrans import Translator


def G_tr(string):
    """
    translate by translate.google.cn
    :param string: a str waiting for translate.
    :return: a str translated form 'string'
    """
    # string = str(input("请输入一段要翻译的文字："))
    translator = Translator(service_urls=['translate.google.cn'])
    result = translator.translate(string, src='en', dest='zh-cn').text
    print(result)
    return result