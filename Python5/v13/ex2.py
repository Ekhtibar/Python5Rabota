def replace_less_than_fifteen(array):
    """
    Заменяет все элементы массива меньше 15 их удвоенными значениями.

    Args:
        array: Массив целых чисел.

    Returns:
        Преобразованный массив.
    """
    for i in range(len(array)):
        if array[i] < 15:
            array[i] *= 2
    return array


def main():
    """
    Основная функция.
    """
    array = [10, 20, 5, 15, 30, 12, 18, 14]
    print(f"Исходный массив: {array}")
    transformed_array = replace_less_than_fifteen(array)
    print(f"Преобразованный массив: {transformed_array}")


if __name__ == "__main__":
    main()