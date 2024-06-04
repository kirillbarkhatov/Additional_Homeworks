# импорт и тестирование функций из дополнительного задания раздела 10.1
from src.funcs_10_1 import get_orders_stats_per_month, sort_products_by_price
from src.orders_list_for_test import orders
from src.products_list_for_test import products

if __name__ == "__main__":
    for product in sort_products_by_price(products, "sweets"):
        print(product)

    print(get_orders_stats_per_month(orders))
