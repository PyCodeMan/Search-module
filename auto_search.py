import requests
from config import headers


def get_info(url, method, data=None, params=None):
    match method:
        case 'POST':
            return requests.post(url=url, data=data)
        case 'GET':
            return requests.get(url=url, params=params)
        case _:
            return None


def auto_search(query):
    google = get_info(f'https://www.google.com/search?hl=ru&gbv=1&q=intext%3A{query}', method='GET', params=headers)
    yandex = get_info(f'https://yandex.ru/search/?text={query}&lr=65&search_source=yacom_desktop_common&rdrnd=144042&redircnt=1703573046.1', method='GET', params=headers)
    izito = get_info(f'https://www.izito.com/search?q={query}', method='GET', params=headers)
    info = (google.text, yandex.text, izito.text)
    return info