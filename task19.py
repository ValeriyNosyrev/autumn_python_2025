import csv

algoritm = [
    "C4.5",
    "k - means",
    "Метод опорных векторов",
    "Apriori",
    "EM",
    "PageRank",
    "AdaBoost",
    "kNN",
    "Наивный байесовский классификатор",
    "CART"
]

with open('algoritm.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки
    writer.writerow(['id', 'значение'])
    # Записываем данные
    for i, value in enumerate(algoritm, start=1):
        writer.writerow([i, value])