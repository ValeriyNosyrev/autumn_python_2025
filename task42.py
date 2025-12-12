# 1. Исключение для некорректного значения в заданном диапазоне
class ValueOutOfRangeError(ValueError):
    def __init__(self, value, min_value, max_value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        message = f"Значение {value} выходит за пределы диапазона от {min_value} до {max_value}"
        super().__init__(message)

# 2. Исключение для случая, когда результат запроса вернул 0 строк

class NoDataError(Exception):
    def __init__(self, query=None):
        self.query = query
        message = "Запрос вернул 0 строк"
        if query:
            message += f"Текст запроса: {query}"
        super().__init__(message)

# 3. Исключение при разрыве соединения с сервером
class ConnectionLostError(ConnectionError):
    def __init__(self, server_address = None, port = None):
        self.server_address = server_address
        self.port = port
        message = f"Соединение с сервером {host}:{port} разорвано"
        if server_address and port:
            message += f"Адрес сервера: {server_address}:{port}"
        super().__init__(message)