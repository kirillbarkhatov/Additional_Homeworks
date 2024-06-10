print(*(x ** 3 for x in range(11) if x % 2 == 0))

def sum_sqr_positive(numbers):
    return sum(x * x for x in numbers if x > 0)


print (*(letter for letter in 'hello' if letter in 'euioa'))

nums = range(21)
nums_3_5 = [x for x in range(21) if x % 3 == 0 or x % 5 ==0]

print(sum(nums_3_5) / len(nums_3_5))


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

print(list(filter(lambda x: x['age'] == 30, people)))