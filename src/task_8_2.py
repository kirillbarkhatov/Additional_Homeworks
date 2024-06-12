import time

def restart(*, times, sec):
    def wrapper(func):
        def inner(*args, **kwargs):
            for i in range(1,times + 1):
                try:
                    print(f'Попытка № {i}')
                    x = func()
                    return x
                except:
                    print(f'Попытка № {i} не удалась')
                time.sleep(sec)
            print('Функцию вызвать не удалось')
        return inner
    return wrapper


@restart(times=4, sec=1)
def test():
    return '2' + 1


print(test())
