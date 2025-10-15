## Считываем все строки из файла
with open('inverted_sort.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Выводим строки в обратном порядке
reversed_lines = lines[::-1]
for line in reversed_lines:
    print(line.strip())

# Дописываем строки в обратном порядке в тот же файл
with open('inverted_sort.txt', 'a', encoding='utf-8') as file:
    file.writelines(reversed_lines)