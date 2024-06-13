import time
from functools import reduce


def timeit(func):
    def wrapper(n):
        print('-')
        time_start = time.time()
        result = func(n)
        delta_time = time.time() - time_start
        print(f'На выполнение затрачено {delta_time}')
        print('-')
        return result

    return wrapper


def slowit(secs=1):
    def wrapper(func):
        def inner(n):
            print('---')
            time.sleep(secs)
            result = func(n)
            print(f'Сработала задержка {secs} секунд')
            print('---')
            return result
        return inner

    return wrapper


def memoize(func):
    cash = {}
    print(cash)
    def wrapper(n):
        print('--')
        if n in cash:
            print(cash)
            print('--')
            return cash[n]
        result = func(n)
        cash[n] = result
        print(cash)
        print('--')
        return result

    return wrapper


def decor(func):
    def wrapper(n):
        print("test")
        return func(n)
    return wrapper


# Без кеширования время работы функции при каждом вызове не менее 2 секунд.
# @timeit
# @slowit(2)
# # @decor
# def product(n):
#     return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None
#
#
# print(product(10))
# print(product(10))

# С кешированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
@timeit
@memoize
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None


print(product(10))
print(product(10))