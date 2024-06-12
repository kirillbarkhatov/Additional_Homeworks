
def generator(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        if type(x) in (list, tuple):
            for i in x:
                yield i
        else:
            yield x
    return wrapper






@generator
def numbers():
    return [2, 3.5, 4.1, 6, 3.2, 7, 3.4]


num = numbers()

print(next(num))
print(next(num))
print(next(num))
print(next(num))