from src.products_and_categories import Product, Category
import pytest


@pytest.fixture
def product_smartphone():
    return Product('Samsung', 'Современный смартфон', 120000.0, 1)


def test_init(product_smartphone):
    assert product_smartphone.name == "Samsung"
    assert product_smartphone.description == "Современный смартфон"
    assert product_smartphone.price == 120000.0
    assert product_smartphone.quantity == 1


@pytest.fixture
def category_smartphone():
    return Category('Смартфон', 'Категория дорогих смартфонов', ["Samsung", 'iPhone', 'Xiaomi'])


def test_category(category_smartphone):
    assert category_smartphone.name == "Смартфон"
    assert category_smartphone.description == "Категория дорогих смартфонов"
    assert category_smartphone.products == ["Samsung", 'iPhone', 'Xiaomi']


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Description 1", 100.0, 10),
        Product("Product 2", "Description 2", 200.0, 5),
        Product("Product 3", "Description 3", 300.0, 3)
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Test Category", "Test Description", sample_products)


def test_category_count(sample_category):
    assert Category.category_count >= 1


def test_product_count(sample_category):
    assert Category.product_count >= 3
