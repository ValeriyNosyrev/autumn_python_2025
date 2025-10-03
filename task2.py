# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

# Преобразование age в число
age_int = int(age)
print("age как число:", age_int)

# Преобразование foo в число не получается ValueError: invalid literal for int() with base 10: '23abc'
# foo_int = int(foo)
# print ("foo как число:", foo_int)

# Преобразуйте переменную age в Boolean
age_str = "123abc"
age_bool = bool(age_str)
# Любая непустая строка — True
print("age как boolean:", age_bool)

# Преобразуйте переменную flag в Boolean
flag = 1
flag_bool = bool(flag)
print("flag как boolean:", flag_bool)

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one_bool = bool(str_one)  # True
str_two_bool = bool(str_two)  # False
# Любая пустая строка — False

print("str_one как boolean:", str_one_bool)
print("str_two как boolean:", str_two_bool)


# Преобразуйте значение 0 и 1 в Boolean
zero_bool = bool(0)
one_bool = bool(1)

print("0 как boolean:", zero_bool)
print("1 как boolean:", one_bool)

# Преобразуйте False в строку
false_str = str(False)
print("False как строка:", false_str)