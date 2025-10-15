def caesar_cipher_char(c, shift):
    """Шифрует один символ кириллического алфавита с заданным сдвигом влево."""
    if 'А' <= c <= 'Я':
        # Шифруем верхний регистр
        idx = ord(c) - ord('А')
        # 33 буквы в русском алфавите
        new_idx = (idx - shift) % 33
        return chr(ord('А') + new_idx)
    elif 'а' <= c <= 'я':
        # Шифруем нижний регистр
        idx = ord(c) - ord('а')
        new_idx = (idx - shift) % 33
        return chr(ord('а') + new_idx)
    else:
        # Не шифруем не-кириллические буквы
        return c

def caesar_cipher_line(line, line_num):
    """Шифрует строку, применяя сдвиг, равный номеру строки (начиная с 1)."""
    shift = line_num
    result = []
    for char in line:
        result.append(caesar_cipher_char(char, shift))
    return ''.join(result)

# Считываем файл и применяем шифр
with open('message.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

encrypted_lines = []
for i, line in enumerate(lines):
    # i начинается с 0, но номер строки с 1
    encrypted_line = caesar_cipher_line(line, i + 1)
    encrypted_lines.append(encrypted_line)

# Выводим зашифрованный текст
for encrypted_line in encrypted_lines:
    print(encrypted_line, end='')