import time
from functools import wraps
from typing import Any, Callable


def benchmark(func: Callable) -> Callable:
    """Декоратор - выводит время, которое было затрачено на выполнение функции"""

    @wraps(func)
    def wrapper(*args: str, **kwargs: str) -> Any:
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res

    return wrapper


def logging(func: Callable) -> Callable:
    """Декоратор - объявляет о том какая функция вызвана"""

    @wraps(func)
    def wrapper(*args: str, **kwargs: str) -> Any:
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func: Callable) -> Callable:
    """Декоратор для подсчета количества вызова функций"""

    @wraps(func)
    def wrapper(*args: str, **kwargs: str) -> Any:
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string: str) -> str:
    """Функция разворачивает строку"""
    return "".join(list(reversed(string)))


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print(reverse_string(text))
print(reverse_string(text * 1000))
