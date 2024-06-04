def sort_products_by_price(products: list[dict], category: str | None = None) -> list[dict]:
    if category != None:
        return [
            product
            for product in sorted(products, key=lambda product: product["price"], reverse=True)
            if product["category"] == category
        ]
    return sorted(products, key=lambda product: product["price"], reverse=True)



