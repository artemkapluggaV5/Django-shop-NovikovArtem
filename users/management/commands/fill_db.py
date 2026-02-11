import random

from django.core.management import BaseCommand
from django.db import transaction
from faker.proxy import Faker

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Скрипт для создания тестовых данных"

    def handle(self, *args, **options):
        faker = Faker(["ru_RU"])

        with transaction.atomic():
            category_list = []

            for _ in range(5):
                category = Category(
                    name=faker.word(),
                    slug=faker.slug(),
                    description=faker.text(),
                    is_active=True,
                )
                category_list.append(category)

            Category.objects.bulk_create(category_list)

            product_list = []

            for _ in range(100):
                product = Product(
                    name=faker.word(),
                    slug=faker.unique.slug(),
                    description=faker.text(),
                    price=random.uniform(10, 5000),
                    category=random.choice(category_list),
                )
                product_list.append(product)

            Product.objects.bulk_create(product_list)

        self.stdout.write(
            self.style.SUCCESS(
                f'Создано {len(category_list)} категорий и {len(product_list)} продуктов'
            )
        )
