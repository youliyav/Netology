import requests
import os

def translate_it(text, lang_from, lang_to, file_to):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1/tr.json/translate?id=46b7fbb9.5c0ae01b.a05ca01a-0-0&srv=tr-text&lang=en-ru'
    # key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    key = 'trnsl.1.1.20161214T114634Z.0492e7b1ebd2d3b4.57c088043e2306103d52f62d96bbf3893cac7554'

    params = {
        'key': key,
        'lang': '-'.join((lang_from, lang_to)),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    with open(file_to, 'w') as f:
        f.write(' '.join(response.get('text', [])))


if __name__ == '__main__':
    files = [f for f in os.listdir("./") if f.endswith(".txt") and not '-ru' in f.lower()]
    for file_name in files:
        lang_from = os.path.splitext(file_name)[0]
        ext = os.path.splitext(file_name)[1]
        lang_to = 'ru'
        file_to = lang_from + '-' + lang_to + ext
        with open(file_name) as f:
            text = f.read()
            translate_it(text, lang_from.lower(), lang_to, file_to)