#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

# Задаём числа для считывания программой
NUM1 :float = float(input("Введите первое число: "))
NUM2 :float = float(input("Введите второе число: "))

# Вычисляем
sum_result: float = NUM1 + NUM2
diff: float = NUM1 - NUM2
quotient: float = NUM1 / NUM2 if NUM2 != 0 else float('inf')  #Делить на 0 нельзя
product: float = NUM1 * NUM2
int_div: int = int(NUM1 // NUM2) if NUM2 != 0 else 0
remainder: float = NUM1 % NUM2 if NUM2 != 0 else float('nan')
power: float = NUM1 ** NUM2

# Получаем результат
print("Сумма:", sum_result)
print("Разность:", diff)
print("Частное:", quotient)
print("Произведение:", product)
print("Результат Целочисленного деления:", int_div)
print("Остаток от деления:", remainder)
print("Результат возведения в степень:", power)