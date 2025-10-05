# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.


x :int = 10
y :int = 15
z :int = 2

# Сравниваем числа

if x >= y and x >= z:
    big = x
elif y >= x and y >= z:
    big = y
else:
    big = z

print("Ответ")
print("Наибольшее число", big)