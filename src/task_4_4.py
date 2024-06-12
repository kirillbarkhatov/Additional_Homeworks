def shorts(func):
    def wrapper(*args, **kwargs):
        words = func(*args, **kwargs).split()
        for i, word in enumerate(words):
            if len(word) > 8:
                words[i] = f'{word[:8]}.'
        return " ".join(words)
    return wrapper


@shorts
def text():
    return '''aaaaaaaaaaaaaaaaaaaaaa bbbbbbbb ccc ddddddddddddddddd'''


print(text())
