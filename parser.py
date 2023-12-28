from bs4 import BeautifulSoup
from auto_search import auto_search


def parser(query):
    google, yandex, izito = auto_search(query)

    parser_google = BeautifulSoup(google, 'lxml')
    parser_yandex = BeautifulSoup(yandex, 'lxml')
    parser_izito = BeautifulSoup(izito, 'lxml')

    google_info = parser_google.find_all('div', class_='egMi0 kCrYT')
    yandex_info = parser_yandex.find_all('a', class_='Link Link_theme_normal OrganicTitle-Link organic__url link')
    izito_info = parser_izito.find_all('a', class_='search-results__link')

    href_list = []
    for tag in google_info:
        href = tag.find('a').get('href')
        href_list.append(href[7:])
    for tag in yandex_info:
        href = tag.get('href')
        href_list.append(href)
    for tag in izito_info:
        href = tag.get('href')
        href_list.append(href)
    return href_list