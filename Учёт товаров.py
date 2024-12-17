from itertools import product
from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name: str = name
        self.weight: float = weight
        self.category: str = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_category(self):
        return self.category

class Shop:
    __file_name = "product2.txt"

    def get_products(self):
        product_file = open(self.__file_name, 'r')
        text_from_file = product_file.read()
        product_file.close()
        return text_from_file

    def add(self, *products):
        product_file = open(self.__file_name, 'r')
        text_from_file = product_file.read()
        product_file.close()
        product_file = open(self.__file_name, 'a')
        for item in products:
            first_string = format(item)
            if first_string in text_from_file:
                print(f'Продукт {item.get_name()} уже есть в магазине')
            else:
                product_file.write(f'{first_string}\n')
        product_file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())