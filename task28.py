def caesar_decrypt (text, shift):
    decrypted = ""
    for char in text:
        # Проверяем, что символ является буквой
        if char.isalpha():
            # Определяем заглавные идли строчные ('a' или 'A')
            base = ord("a") if char.islower() else ord("A")
            # Дешифруем символ
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            # Если символ не буква, оставляем его без изменений
            decrypted += char
    return decrypted

encrypted_line = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

print("Возможные варианты: ")
print ("-" * 30)
for shift in range(26):
    decrypted_line = caesar_decrypt(encrypted_line, shift)
    print(f"Смещение {shift}: {decrypted_line}")

print ("-" * 30)
# Осмысленный текст получается на 6 строке, выводим
correct_shift = 6
final_decription = caesar_decrypt(encrypted_line, correct_shift)
print(f"Исходная строка: {final_decription}")
