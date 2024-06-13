def shorts(symbs, *, symb):
    def wrapper(func):
        def inner(*args, **kwargs):
            words = func(*args, **kwargs).split()
            for i, word in enumerate(words):
                if len(word) > symbs:
                    words[i] = f'{word[:symbs]}{symb}'
            return " ".join(words)
        return inner
    return wrapper


@shorts(3, symb="4")
def text():
    return '''aaaaaaaaaaaaaaaaaaaaaa bbbbbbbb ccc ddddddddddddddddd'''


print(text())



