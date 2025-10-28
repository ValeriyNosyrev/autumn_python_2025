import json
import csv
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from datetime import datetime
from io import StringIO
from jinja2 import Environment, FileSystemLoader
import os

# Создаём абстрактный базовый класс DataExporter:
class DataExporter(ABC):
    @abstractmethod
    # Экспортирует данные в соответствующий формат.
    def export(self, data):
        pass

    @abstractmethod
    # Возвращает название формата.
    def get_format_name(self):
        pass

    # Проверяет, что данные не пустые.
    def validate_data(self, data):
        if not data:
            raise ValueError("Данные не могут быть пустыми.")

# Создаем классы для каждого формата:
class JSONExporter(DataExporter):
    def get_format_name(self):
        return "JSON"

    def export(self, data):
        self.validate_data(data)
        export_data = {
            "data": data,
            "export_timestamp": datetime.now().isoformat()
        }
        print(json.dumps(export_data, indent=2, ensure_ascii=False))

class CSVExporter(DataExporter):
    def get_format_name(self):
        return "CSV"
    def export(self, data):
        self.validate_data(data)
        # Убеждаемся, что data — это список, и каждый элемент — словарь. Иначе CSV не построится корректно.
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Данные должны быть списком словарей.")

        # Создаём "виртуальный файл" в памяти для записи CSV.
        output = StringIO()
        # Берём ключи первого словаря — они станут заголовками таблицы.
        fieldnames = data[0].keys()
        # Создаём объект для записи словарей в CSV, указывая заголовки.
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        # Записываем первую строку — заголовки.
        writer.writeheader()
        # Записываем все строки данных.
        writer.writerows(data)
        # Выводим содержимое "виртуального файла" в консоль.
        print(output.getvalue())

class XMLExporter(DataExporter):

    def get_format_name(self):
        return "XML"

    def export(self, data):
        self.validate_data(data)
        # Проверка на пустоту данных
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Данные должны быть списком словарей!")

        # Создаем корневой узел XML "report"
        root = ET.Element("report")
        # Добавляем узлы для каждого словаря в списке данных
        for item in data:
            # Создаём дочерний тег "product" для данных
            product = ET.SubElement(root, "product")
            for key, value in item.items():
                elem = ET.SubElement(product, key)
                elem.text = str(value)

        # Выводим XML в консоль
        print(ET.tostring(root, encoding="unicode"))

class HTMLExporter(DataExporter):
    def get_format_name(self):
        return "HTML"

    def export(self, data):
        self.validate_data(data)
        # Проверка на пустоту данных
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Данные должны быть списком словарей!")

        headers = list(data[0].keys())

        # Настраиваем Jinja2
        template_dir = os.path.dirname(__file__)
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("task41.html")

        # Выводим
        html_output = template.render(headers=headers, data=data)
        print(html_output)


# Этот код должен работать после реализации:
sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10}
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter(),
    HTMLExporter()
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")