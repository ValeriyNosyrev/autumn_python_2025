def numbers_to_letters(text):
    result = []
    for letter in text.split(" "):
        #Чек, является ли символ числом
        if letter.isdigit():
            number = int(letter)
            # Проверяем в диапазоне от 1 до 26
            if 1 <=number<=26:
              # Получаем букву из числа
                letter = chr(ord("a") + number - 1)
                result.append(letter)
            else:
            # Числа вне диапазона не изменять.
               result.append(letter)
        else:
            #Не числа не изменять (запятые, точки и проч).
            result.append(letter)

    return "".join(result)

input1 = "8 5 12 12 15"
input2 = "8 5 12 12 15 , 0 23 15 18 12 4 !"

print(numbers_to_letters(input1))
print(numbers_to_letters(input2))