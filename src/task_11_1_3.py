def primes():
    """Генератор, который генерирует последовательность простых чисел."""
    primes_list = [2, 3]
    yield primes_list[0]
    yield primes_list[1]
    find_next_prime = 3
    while True:
        find_next_prime += 1
        cnt_div = 0
        for i in primes_list:
            if find_next_prime % i == 0:
                cnt_div += 1

        if cnt_div == 0:
            yield find_next_prime
            primes_list.append(find_next_prime)




p = primes()
for i in range(10):
    print(next(p))