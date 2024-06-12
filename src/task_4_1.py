def is_even(func):
    def check_even():
        result = round(func())
        return result
    return check_even


def check_integers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result
    return wrapper

@check_integers
def numbers():
    return [2, 3.5, 4.1, 6, 3.2, 7, 3.4]



@is_even
def number(x):
    return x


num = numbers()

print(numbers())