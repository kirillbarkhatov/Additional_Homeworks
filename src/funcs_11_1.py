def non_empty_truths(input_data:list) -> list:
    """Функция с помощью генераторов списков должна вычислять копию входного списка списков,
    «очищенную» от ложных элементов (False, любые пустые коллекции, 0 и None-значения),
    а заодно и от пустых списков — такие могу присутствовать сами по себе
    или могут получаться после отбрасывания из них всех элементов.
    """
    result = [data for data in input_data if data]
    for i in range(len(result)):
        result[i] = [data for data in result[i] if data]
    result = [data for data in result if data]
    return result


def my_map(f, xs: list) -> list:
    """Упрощенный map"""
    for i in range(len(xs)):
        xs[i] = f(xs[i])
    return xs


def my_filter(f, xs):
    """Упрощенный filter"""

    return [x for x in xs if f(x)]


def replicate_each(n, xs):
    """Функция для каждого элемента итератора xs  выдает на выход по n копий этого элемента"""
    return [i for x in xs for i in [x for j in range(n)]]



if __name__ in "__main__":
    print(non_empty_truths([]))
    # []
    print(non_empty_truths([[], []]))
    # []
    print(non_empty_truths([[0]]))
    # []
    print(non_empty_truths([[0, ""], [False, None]]))
    # []
    print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))
    # [[1, 2], [True, 42]]

    print(list(my_map(lambda x: x + 2, [-1, 2, -3])))  # [1, 4, -1]
    print(list(my_filter(lambda x: x % 2 == 1, range(10))))  # [1, 3, 5, 7, 9]
    print(list(replicate_each(1, [1, 'a'])))  # [1, 'a']
    print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
    print(list(replicate_each(0, [1, 'a'])))  # []