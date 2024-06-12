def atntn(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return text.replace('!', '!!!')
    return wrapper


def qtsn(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return text.replace('?', '???')
    return wrapper


def dot(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return text.replace('.', '...')
    return wrapper


@atntn
@qtsn
@dot
def texts():
    return 'dhfbv! jhbjhb! kjhbkjhbjh. jhbhb? kjhbhbjjh. jhbhb!'

print(texts())