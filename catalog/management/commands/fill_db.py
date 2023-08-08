from django.core.management import BaseCommand, call_command
from catalog.models import Product, Category
from django.apps import apps
from pathlib import Path
from django.db import connection
from django.db import transaction
import json


class Command(BaseCommand):
    products_path = Path('./catalog/catalog_filling/products.json')
    categories_path = Path('./catalog/catalog_filling/categories.json')

    @staticmethod
    def read_datafile(data_path):
        if data_path.exists() and data_path.is_file():
            try:
                with open(data_path, 'r', encoding='UTF-8') as json_file:
                    return json.load(json_file)
            except Exception:
                return

    @staticmethod
    def clear_db(models):
        # очищаем старые значения БД
        with transaction.atomic():
            for model in models:
                model.objects.all().delete()

    @staticmethod
    def reset_sequence(models):
        for model in models:
            table_name = model._meta.db_table
            sequence_name = f"{table_name}_id_seq"
            with connection.cursor() as cursor:
                cursor.execute(f"ALTER SEQUENCE {sequence_name} RESTART WITH 1;")
                connection.commit()

    def handle(self, *args, **options):
        app_name = self.__module__.split('.')[0]
        app_config = apps.get_app_config(app_name)
        models = tuple(app_config.get_models())

        # очищаем старые значения БД и сбрасываем счетчик
        self.clear_db(models)
        self.reset_sequence(models)

        categories = self.read_datafile(self.categories_path)
        products = self.read_datafile(self.products_path)

        for category_info in categories:
            name = category_info.get('name')
            category = Category(**category_info)
            category.save()
            products_info = []
            for product in products:
                if product.get('category') == name:
                    product['category'] = category
                    products_info.append(Product(**product))
            Product.objects.bulk_create(products_info)
