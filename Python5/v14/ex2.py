def replace_above_average(array):
    """
    Определяет среднее арифметическое и заменяет элементы больше среднего на 1.

    Args:
        array: Массив целых чисел.

    Returns:
        Преобразованный массив.
    """
    average = sum(array) / len(array)
    for i in range(len(array)):
        if array[i] > average:
            array[i] = 1
    return array


def main():
    """
    Основная функция.
    """
    array = []
    print("Введите 10 целых чисел:")
    for _ in range(10):
        number = int(input())
        array.append(number)

    print(f"Исходный массив: {array}")
    transformed_array = replace_above_average(array)
    print(f"Преобразованный массив: {transformed_array}")


if __name__ == "__main__":
    main()