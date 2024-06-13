from functools import wraps


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} called with args: {args} and kwargs {kwargs}. Result: {result}')
        return result

    return wrapper



@logging
def multiply(x, y):
    return x * y
multiply(2, 3)
# >>> Function multiply called with args: (2, 3) and kwargs: {}. Result: 6