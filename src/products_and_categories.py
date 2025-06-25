class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products: list = None):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        if products is not None:
            for existing_product in products:
                if existing_product.name.lower() == name.lower():
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    return existing_product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if self.__price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        if new_price < self.__price:
            answer = input(
                f"Вы снижаете цену с {self.__price} до {new_price}. "
                "Подтвердите действие (y/n): "
            ).strip().lower()

            if answer != 'y':
                print("Отмена: цена не изменена")
                return

        self.__price = new_price
        print(f"Цена обновлена: {self.__price}")


class Category:
    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def products_read(self):
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products)
