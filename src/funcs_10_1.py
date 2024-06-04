def sort_products_by_price(products: list[dict], category: str | None = None) -> list[dict]:
    """Функция принимает на вход список словарей, состоящих из данных о продуктах в магазине
    и возвращает список словарей, отсортированных по убыванию стоимости продукта,
    но только для продуктов из заданной категории. Если категория не задана,
    то сортировка производится для всех продуктов
    """

    if category != None:
        return [
            product
            for product in sorted(products, key=lambda product: product["price"], reverse=True)
            if product["category"] == category
        ]
    return sorted(products, key=lambda product: product["price"], reverse=True)


def get_orders_stats_per_month(orders: list[dict]) -> list[dict]:
    """Функция принимает на вход список словарей, представляющих информацию о заказах в интернет-магазине
    и возвращает словарь, содержащий информацию о средней стоимости заказа и количестве заказов за каждый месяц
    """

    orders_stats_per_month = {}
    for order in orders:
        order['YYYY-MM'] = order['date'][:7]
        order['order_value'] = 0
        for item in order['items']:
            order['order_value'] += item['price'] * item['quantity']
        orders_stats_per_month[order['YYYY-MM']] = {'average_order_value': 0, 'order_count': 0}

    for order in orders:
        orders_stats_per_month[order['YYYY-MM']]['order_count'] += 1
        orders_stats_per_month[order['YYYY-MM']]['average_order_value'] += order['order_value']

    for month in orders_stats_per_month:
        orders_stats_per_month[month]['average_order_value'] = round(
                orders_stats_per_month[month]['average_order_value'] / orders_stats_per_month[month]['order_count'],
                2
        )

    return orders_stats_per_month