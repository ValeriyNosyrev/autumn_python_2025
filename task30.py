prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]


EXCHANGE_PRICES = {
    "USD" : 81.06,
    "EUR" : 94.90,
    "JPY" : 0.54,
    "RUB" : 1.0,
}
def convert_rubles(price_str):
    price_str = price_str.strip()

    # Проверяем на числовые значения
    try:
        return float(price_str)
    except ValueError:
        pass

    # Проверяем по символу валюты
    if price_str.startswith("₽"):
        try:
            return float(price_str[1:])
        except ValueError:
            return None

    elif price_str.endswith("USD"):
        try:
            value = float(price_str[:-3].strip())
            return value * EXCHANGE_PRICES["USD"]
        except ValueError:
            return None

    elif price_str.startswith("€"):
        try:
            value = float(price_str[1:].strip())
            return value * EXCHANGE_PRICES["EUR"]
        except ValueError:
            return None

    elif price_str.startswith("$"):
        try:
            value = float(price_str[1:].strip())
            return value * EXCHANGE_PRICES["USD"]
        except ValueError:
            return None

    elif price_str.startswith("¥"):
        try:
            value = float(price_str[1:].strip())
            return value * EXCHANGE_PRICES["JPY"]
        except ValueError:
            return None

rubles_prices = [
    convert_rubles(price)
    for price in prices
    if convert_rubles(price) is not None
]

print(rubles_prices)