users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Вводим тип сортировки
sort_type = int(input("тип сортировки: "))

# Вводим критерии поиска
criteria = input("Введите критерии поиска: ")

# Приведём критерии к нужному типу
if sort_type == 1:
    criteria = int(criteria)

# Фильтруем пользователей
filtered_users = []

for user_ in users:
    if sort_type == 1:  # По возрасту
        if user_['age'] > criteria:
            filtered_users.append(user_)
    elif sort_type == 2:  # По первой букве логина
        if user_['login'][0] == criteria:
            filtered_users.append(user_)
    elif sort_type == 3:  # По группе
        if user_['group'] == criteria:
            filtered_users.append(user_)

# Выводим результат
for user in filtered_users:
    age = user['age']
    ending = 'лет' if age % 10 == 0 or 5 <= age % 10 <= 9 or 11 <= age % 100 <= 19 else 'год' if age % 10 == 1 else 'года'
    print(f"Пользователь: '{user['login']}' возраст {user['age']} {ending}, группа \"{user['group']}\"")