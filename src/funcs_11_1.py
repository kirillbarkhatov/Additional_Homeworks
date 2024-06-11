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