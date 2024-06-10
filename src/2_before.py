def collatz_list(n:int) -> list:
    """Колдуем, пока не получим стемень двойки"""
    result = []
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            result.append(n)
            yield n
        if n == 1:
            break



if __name__ == '__main__':
    n = 27
    gen = collatz_list(n)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
