def plus_one(arr):
# Создаём новый массив, в который будем записывать увеличенные значения
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i] + 1)
    return new_arr


# Пример использования
mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
new_mass = plus_one(mass)

print("Исходный массив:", mass)
print("Преобразованный массив:", new_mass)