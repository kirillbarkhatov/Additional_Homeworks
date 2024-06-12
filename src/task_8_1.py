def check_integers(precision):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            # Проверка на тип с использованием type()
            if type(result) == float:
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [round(x, precision) if type(x) == float else x for x in result]
                # Возвращаем тот же тип, что и исходный (list или tuple)
                return type(result)(rounded)
            else:
                return result
        return inner
    return wrapper

@check_integers(2)
def numbers():
    return [2, 3.5, 4.1, 6, 3.2658, 7, 3.4]


print(numbers())