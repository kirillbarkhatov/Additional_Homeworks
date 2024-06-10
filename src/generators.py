# print(*(x ** 3 for x in range(11) if x % 2 == 0))
#
# def sum_sqr_positive(numbers):
#     return sum(x * x for x in numbers if x > 0)
#
#
# print (*(letter for letter in 'hello' if letter in 'euioa'))
#
# nums = range(21)
# nums_3_5 = [x for x in range(21) if x % 3 == 0 or x % 5 ==0]
#
# print(sum(nums_3_5) / len(nums_3_5))
#
#
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 30},
#     {"name": "Eve", "age": 25},
# ]
#
# print(list(filter(lambda x: x['age'] == 30, people)))
#
#
# def sqr_generator(nums):
#     for num in nums:
#         yield num ** 2
#
#
# import random
#
#
# def rndm(a=10, b=15):
#     while True:
#         yield random.randint(a, b)
#
# i = rndm()
# print(next(i))
# print(next(i))
# print(next(i))
#
#
# def formula_gen():
#     pass
#
#
# def chain_lists(list1, list2):
#     for i in list(set(list1) & set(list2)):
#         yield i


def spiral_generator(n):
    matrix = [[0] * n for i in range(n)]
    print(matrix)
    x, y = n//2, n//2
    print(x, y)
    matrix[y][x] = 1
    yield matrix[y][x]

    for i in range(2, n*n+1):
        if x == y or (x < y and x + y < n-1) or (x > y and x + y >= n):
            dx, dy = 0, -1
        else:
            dx, dy = -1, 0
        x, y = x+dx, y+dy
        print(x,y)
        matrix[y][x] = i
        yield matrix[y][x]


matrix = spiral_generator(5)
for j in range(25):
    print(next(matrix))
