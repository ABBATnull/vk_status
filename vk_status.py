#мой id в вк 195777006

import vk
import requests

from bs4 import BeautifulSoup

def vk_oath_n_status_posting(string):
 access_token = 'bf012164c88f5aa88f7368chip45d4a15cfc5b2133ngw26ca4bf1qplmna6915ab84d6i96d330eipklah67'
 v = '5.95'

 # Подключение к VK API
 session = vk.Session(access_token=access_token)
 api = vk.API(session, v=v)
 api.status.set (user_id = 195777006, text = string)

def parsing_weather_dol_course():
 url_bank = 'https://finance.rambler.ru/currencies/'
 url_weather=
'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA%D0%B5,_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B0%D0%B9'
 response_bank = requests.get(url_bank)
 response_weather = requests.get(url_weather)
 soup_bank = BeautifulSoup(response_bank.text, 'html')
 soup_weather = BeautifulSoup(response_weather.text, 'html')
 dollar_course_table = soup_bank.find('div', class_='finance-exchange-rate__value')
 weather_value = soup_weather.find('span', class_='t_0', style = 'display: block;').text
 status_str = 'Курс доллара на сегодня: ' + dollar_course_table.text + ', за бортом ' + weather_value
 vk_oath_n_status_posting(status_str) #кидаем в статус вк

def main ():
 parsing_weather_dol_course () #парсим сайты погоды и курса евро с баксом
if __name__ == "__main__":
 main()