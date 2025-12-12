from datetime import datetime
import os
import threading

#Блокировка, для безопасности файла логирования
lock = threading.Lock()

def count_uses(func):
    # Храним счетчик вызовов в атрибуте функции
    if not hasattr(func, 'call_count'):
        func.call_count = 0

    def wrapper(*args, **kwargs):
        # Увеличиваем счетчик вызовов
        func.call_count += 1

        # Получаем текущее время
        current_time = datetime.now().strftime('%d.%m.%Y %H:%M')

        # Записываем в файл логирования
        with lock:
            # Форматируем строку для записи
            log_entry = f'{func.__name__}, {func.call_count}, {current_time}'

            # Записываем в файл логирования
            with open('../debug.log', 'a', encoding='utf-8') as log_file:
                log_file.write(log_entry + '\n')

        # Вызываем оригинальную функцию
        return func(*args, **kwargs)
    # Сохраняем метаданные функции
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

# Тестирование декоратора

@count_uses
def render(text):
    return text.upper()

@count_uses
def create_user(**user_data):
    profile = 'Пользователь:\n'
    for key, value in user_data.items():
        profile += f'{key.capitalize()}: {value}\n'
    return profile

@count_uses
def processing(data, *filters, verbose=False, **options): # Комбинированная функция с позиционными, именованными аргументами и переменным числом аргументов обоих типов
    result = f'Анализируем данные: {len(data)}'
    if verbose:
        result += f'\nФильтры: {len(filters)}\nОпции: {len(options)}'
        return result


if __name__ == '__main__':
    # Очищаем файл перед началом тестирования
    if os.path.exists('../debug.log'):
        os.remove('../debug.log')

    # Вызываем функции несколько раз
    print(render("test"))  # TEST
    print(render("hello world"))  # HELLO WORLD
    print(create_user(name='Vasya', age=42, city = 'Petrushevo'))
    print(create_user(name='Tanya', age=22, email='tatka@mail.ru'))

    data = [1, 2, 3, 4, 5]
    print(processing(data))
    print(processing(data, 'filter1', 'filter2', verbose=True, max_items=10))

    print("\nСтатистика вызовов записана в файл debug.log")
    print("Содержимое файла:")

    with open('../debug.log', 'r', encoding='utf-8') as log_file:
        print(log_file.read())