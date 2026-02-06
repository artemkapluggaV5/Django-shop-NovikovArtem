from decimal import Decimal
import pytest
from catalog.models import Category, Product

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="Электроника", slug="elektronika", description="Описание категории")
    assert Category.objects.count() == 1
    assert category.name == "Электроника"
    assert category.is_active is True

@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(name="Смартфоны", slug="smartphones")
    product = Product.objects.create(
        category=category,
        name="iPhone 15",
        slug="iphone-15",
        price=Decimal("95000.00")
    )
    assert Product.objects.count() == 1
    assert product.name == "iPhone 15"
    assert product.price == Decimal("95000.00")

@pytest.mark.django_db
def test_category_edit():
    category = Category.objects.create(name="Старая", slug="old")
    category.name = "Новая"
    category.save()
    assert Category.objects.get(id=category.id).name == "Новая"

@pytest.mark.django_db
def test_category_delete():
    category = Category.objects.create(name="На удаление", slug="del")
    category.delete()
    assert Category.objects.count() == 0

@pytest.mark.django_db
def test_product_edit():
    category = Category.objects.create(name="Кат", slug="cat")
    product = Product.objects.create(category=category, name="Хлеб", slug="bread", price=50)
    product.price = Decimal("60.00")
    product.save()
    assert Product.objects.get(id=product.id).price == Decimal("60.00")

@pytest.mark.django_db
def test_product_delete():
    category = Category.objects.create(name="Кат", slug="cat")
    product = Product.objects.create(category=category, name="Хлеб", slug="bread", price=50)
    product.delete()
    assert Product.objects.count() == 0

@pytest.mark.django_db
def test_cascade_delete_logic():
    category = Category.objects.create(name="Техника", slug="tech")
    Product.objects.create(category=category, name="Телефон", slug="phone", price=100)
    category.delete()
    assert Product.objects.count() == 0