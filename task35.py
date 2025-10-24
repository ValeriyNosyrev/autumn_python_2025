class Temperature:
    def __init__(self, celsius =0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273.15

def main():
    try:
        celsius_input = float(input("Введите температуру в градусах по Цельсию: "))
    except ValueError:
        print("Введите числовое значение!")
        return

    temp = Temperature(celsius_input)
    print("Температура в градусах по Цельсию:", temp.celsius)
    print("Температура в градусах по Фаренгейту:", temp.fahrenheit)
    print("Температура в градусах по Кельвину:", temp.kelvin)

if __name__ == '__main__':
    main()