# Установка и базовое использование
# https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start
from bs4 import BeautifulSoup
import requests
import json

# Получение HTML страницы URI
url = "https://python-academy.org/ru/guide/oop"
response = requests.get(url)
html = response.text
#  То что ищем в html
# <li><strong class="sc-7bcc833-0 VfRFo">Модульность</strong> — код разделен на логические блоки (классы), которые легче понимать и поддерживать</li>
soup = BeautifulSoup(html, 'html.parser')

# Найти все элементы li в контейнере OL
elements = soup.select('ol > li')
mass = []
for row in elements:
    mass.append(row.text.split("—")


# Сериализуем массив в json формат и сохранем в файле
fd = open("db.py", "w")
json.dump(mass, fd)
fd.close()