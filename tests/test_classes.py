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


@pytest.fixture
def sample_product_data():
    return {
        'name': 'Xiaomi',
        'description': 'Недорогой смартфон',
        'price': 25000.0,
        'quantity': 3
    }


@pytest.fixture
def existing_products():
    return [
        Product('Samsung', 'Флагман', 120000.0, 2),
        Product('Xiaomi', 'Старая модель', 20000.0, 5)
    ]


def test_new_product_without_existing(sample_product_data):
    new_product = Product.new_product(sample_product_data)

    assert new_product.name == 'Xiaomi'
    assert new_product.description == 'Недорогой смартфон'
    assert new_product.price == 25000.0
    assert new_product.quantity == 3


def test_new_product_with_existing(sample_product_data, existing_products):
    updated_product = Product.new_product(sample_product_data, existing_products)

    assert updated_product.name == 'Xiaomi'
    assert updated_product.price == 25000.0
    assert updated_product.quantity == 8
    assert len(existing_products) == 2


def test_new_product_with_empty_list(sample_product_data):
    new_product = Product.new_product(sample_product_data, [])

    assert new_product.name == 'Xiaomi'
    assert new_product.quantity == 3


@pytest.fixture
def empty_category():
    return Category("Телефоны", "Мобильные устройства", products=[])


@pytest.fixture
def sample_product():
    return Product("iPhone", "Смартфон", 100000.0, 5)


def test_add_product_successfully(empty_category, sample_product):
    """Альтернативный вариант, если products - приватное поле"""
    initial_count = len(empty_category._Category__products)

    empty_category.add_product(sample_product)

    assert len(empty_category._Category__products) == initial_count + 1
    assert empty_category._Category__products[-1].name == "iPhone"


def test_price(sample_product):
    assert sample_product.price == 100000.0  # Проверяем получение цены


def test_set_price_lower_with_confirmation(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    sample_product.price = 40000.0
    assert sample_product.price == 40000.0  # Цена должна измениться


def test_set_price_lower_without_confirmation(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'n')

    original_price = sample_product.price
    sample_product.price = 40000.0
    assert sample_product.price == original_price


@pytest.fixture
def category_with_products():
    products = [
        Product("MacBook Pro", "Apple", 150000.0, 5),
        Product("ThinkPad", "Lenovo", 80000.0, 10)
    ]
    return Category("Ноутбуки", "Портативные компьютеры", products=products)


def test_get_products(category_with_products):
    products = category_with_products.products

    assert isinstance(products, list)
    assert len(products) == 2
    assert products[0].name == "MacBook Pro"
    assert products[1].name == "ThinkPad"


def test_products_read(category_with_products):
    output = category_with_products.products_read

    expected_lines = [
        "MacBook Pro, 150000.0 руб. Остаток: 5 шт.",
        "ThinkPad, 80000.0 руб. Остаток: 10 шт."
    ]
    for line in expected_lines:
        assert line in output
    assert output.count("\n") == 1