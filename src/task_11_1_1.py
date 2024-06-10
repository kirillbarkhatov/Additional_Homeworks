def filter_orders_by_cost(file, cost):
    head_row = next(file)
    print(head_row)
    rows = [row for row in file]
    print(rows)


with open("orders.csv", "r") as f:
    result = filter_orders_by_cost(f, 20)

print(result)