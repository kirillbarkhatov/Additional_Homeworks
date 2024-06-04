from src.funcs_10_1 import sort_products_by_price
from src.products_list_for_test import products
from src.orders_list_for_test import orders


if __name__ == '__main__':
    for product in sort_products_by_price(products, 'sweets'):
        print(product)
