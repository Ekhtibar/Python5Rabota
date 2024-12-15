def find_negative_pairs(array):
    """
    Находит и выводит пары отрицательных чисел, стоящих по порядку.

    Args:
        array: Массив целых чисел.
    """
    negative_pairs = []
    for i in range(len(array) - 1):
        if array[i] < 0 and array[i + 1] < 0:
            negative_pairs.append((array[i], array[i + 1]))

    return negative_pairs


def main():
    """
    Основная функция.
    """
    array = [-1, -2, 3, -4, -5, 6, -7, -8, 9, 10]
    pairs = find_negative_pairs(array)
    print(f"Исходный массив: {array}")
    print(f"Пары отрицательных чисел: {pairs}")


if __name__ == "__main__":
    main()