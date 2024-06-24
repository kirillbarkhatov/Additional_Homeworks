import json, random

def generate_users(first_names, last_names, cities):
    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randrange(18, 65)
        city = random.choice(cities)
        yield {'first_name': first_name, 'last_name': last_name, 'age': age, 'city': city}


first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Mia']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']


users = generate_users(first_names, last_names, cities)

# print(next(users))
# print(next(users))
# print(next(users))
# print(next(users))
# print(next(users))

users_list = [next(users) for i in range(5)]
# print(users_list)

json_data = json.dumps(users_list, indent=4)
print(json_data)
