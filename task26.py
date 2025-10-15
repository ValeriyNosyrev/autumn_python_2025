#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

glas_set = set("аяуюоеёэиыАЯУЮОЕЁЭИЫ")

# Инициализируем словарь для подсчета гласных
glas_counts = {}

# Открываем файл dump.txt для чтения (предполагаем кодировку utf-8)
try:
    with open('dump.txt', 'r', encoding='utf-8') as f:
        # Читаем весь текст из файла
        text = f.read()
# Завершаем программу, если файл не найден
except FileNotFoundError:
    print("Файл dump.txt не найден.")
    exit()

# Проходим по каждому символу в тексте
for char in text:
    # Проверяем, является ли символ гласной буквой
    if char in glas_set:
        # Приводим символ к нижнему регистру для учета в словаре
        lower_char = char.lower()
        # Увеличиваем счетчик для этой гласной буквы
        glas_counts[lower_char] = glas_counts.get(lower_char, 0) + 1

# Сортируем гласные по алфавиту для вывода
sorted_glas = sorted(glas_counts.keys())

# Выводим статистику
for glas in sorted_glas:
    count = glas_counts[glas]
    print(f"Количество букв {glas} - {count}")

