import os
import json


def log_filter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        count = len(result)
        sum_tr = sum([tr["amount"] for tr in result])
        print(f'Кол-во - {count}, сумма - {sum_tr}')
        return result
    return wrapper



@log_filter
def get_filtered_file(file):
    transactions = json.load(file)
    filtered_transactions = list(filter(lambda x: x['currency'] == 'USD', transactions))
    return filtered_transactions




if __name__ == "__main__":
    project_dir = os.path.dirname(os.getcwd())
    data_dir = os.path.join(project_dir, "data")
    name_file_path = os.path.join(data_dir, "transactions.json")
    with open(name_file_path, "r") as file:
        filtered_transactions = get_filtered_file(file)


    with open(os.path.join(data_dir, "transactions_filtered.json"), "w") as filtered_file:
        json.dump(filtered_transactions, filtered_file, indent=4)