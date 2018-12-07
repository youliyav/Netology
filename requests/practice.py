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

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20181203T174752Z.949933b6bd21e319.3735be4a82be1a600f791f625513c1a4ccdb7403'

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