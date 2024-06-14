def memoized(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result

        return result

    return wrapper


def memoizing(depth_save):
    def wrapper(func):
        cache = {}
        func_call = [0]
        cache_calls = {}
        def inner(n):
            if n in cache:
                return cache[n]["result"]
            result = func(n)
            func_call[0] += 1
            cache[n] = {"save_number": func_call[0], "result": result}
            cache_calls[n] = func_call[0]
            for n in cache:
                if cache[n]["save_number"] == min(cache_calls.values()) and len(cache) > depth_save:
                    del cache[n]
                    del cache_calls[n]
                    break
            return result

        return inner


    return wrapper


print('-------MEMOIZED---------')
@memoized
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))
# >>> Calculating...
#     10
print(f(1))
# >>> 10
print(f(42))
# >>> Calculating...
#     420
print(f(42))
# >>> 420
print(f(1))
# >>> 10


print('-------MEMOIZING---------')
@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
# >>> Calculating...
#     10
print(f(1))  # Будет «вспомнено»
# >>> 10
print(f(2))
# >>> Calculating...
#     20
print(f(3))
# >>> Calculating...
#     30
print(f(4))  # Вытеснит запомненный результат для «1»
# >>> Calculating...
#     40
print(f(1))  # Будет перевычислено
# >>> Calculating...
#     10