# Класс DB как синглтон для подключения к PostgreSQL

import psycopg2

class DB: # Класс DB как синглтон для подключения к PostgreSQL
    __instance = None

    def __new__(cls, *args, **kwargs): # Метод __new__ для контроля синглтона
        if cls.__instance is None:
            cls.__instance = super(DB, cls).__new__(cls)
        return cls.__instance

    def __init__(self, dbname = None, user = None, password = None, host = 'localhost', port = 5432):
        # Инициализация подключения к БД
        # Проверяем, не было ли уже установки соединения
        if not hasattr(self, 'connection'):
            try:
                self.connection = psycopg2.connect(dbname = dbname, user = user, password = password, host = host, port = port)
                print(f'Соединение с БД {dbname} установлено')
            except psycopg2.Error as e:
                print(f'Ошибка подключения к БД {dbname}: {e}')
                self.connection = None

    @staticmethod
    def get_instance(dbname = None, user = None, password = None, host = 'localhost', port = 5432):
        if DB.__instance is None:
            DB(dbname, user, password, host, port)
        return DB.__instance

    def get_connection(self):
        # Метод для получения объекта соединения
        return self.connection

    def close(self):
        # Метод для закрытия соединения и сброса
        if self.connection:
            self.connection.close()
            print('Соединение с БД закрыто')
            # Сбрасываем экземпляр для возможности создания нового подключения
            DB.__instance = None

# Абстрактный класс Car с фабрикой и абстрактными методами
import abc
from abc import ABC, abstractmethod

class Car(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def create_lada(cls):
        return cls("Lada", "Vesta")

    @classmethod
    def create_mercedes(cls):
        return cls("Mercedes", "S-class")

    @classmethod
    def create_toyota(cls):
        return cls("Toyota", "Camry")

    def __repr__(self):
        return f"{self.brand} {self.model}"

    @abstractmethod
    def sold(self):
        pass

    @abstractmethod
    def discount(self):
        pass

class RealisedClassCar(Car):

    def sold(self):
        print(f'Автомобиль {self.brand} {self.model} продан')

    def discount(self):
        print(f'На автомобиль {self.brand} {self.model}  скидка 5%')