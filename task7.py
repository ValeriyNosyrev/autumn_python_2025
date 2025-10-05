#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

# Задаём значения
A :float = float (input("Введите координаты точки А: "))
B :float = float (input("Введите координаты точки В: "))
C :float = float (input("Введите координаты точки С: "))

# Находим длины отрезков

length_AC :float = abs (A - C)
length_BC :float = abs (B - C)
total_length :float = length_AC + length_BC

# Выводим результат

print("Длина отрезка AC: ", length_AC)
print("Длина отрезка BC: ", length_BC)
print("Сумма отрезков AC и DC: ", total_length)
