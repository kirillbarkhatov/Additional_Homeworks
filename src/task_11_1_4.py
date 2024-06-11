def fibonacci():
    fibonacci_list = [0, 1]
    yield fibonacci_list[0]
    yield fibonacci_list[1]
    while True:
        result = fibonacci_list[-1] + fibonacci_list[-2]
        yield result
        fibonacci_list.append(result)

f = fibonacci()
for i in range(10):
    print(next(f))