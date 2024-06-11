def filter_orders_by_cost(file, cost):
    head_row = next(file)
    rows = [row.split(';') for row in file]
    clients = [int(row[0].rstrip()) for row in rows]
    orders = [int(row[1].rstrip()) for row in rows]
    costs = [float(row[2].rstrip()) for row in rows]
    return [f'{clients[i]}, {orders[i]}, {costs[i]}' for i in range(len(rows))]


with open("orders.csv", "r") as f:
    result = filter_orders_by_cost(f, 20)

print(result)