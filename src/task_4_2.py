import time


def restart(func):
    def wrapper(*args, **kwargs):
        for i in range(1,4):
            try:
                print(f'Попытка № {i}')
                x = func()
                return x
            except:
                print(f'Попытка № {i} не удалась')
            time.sleep(3)
        print('Функцию вызвать не удалось')
    return wrapper


@restart
def test():
    return '2' + 1


print(test())
