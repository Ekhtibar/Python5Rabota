def transform_array(array):
    """
    Преобразует массив по заданным условиям.

    Args:
        array: Массив целых чисел.

    Returns:
        Преобразованный массив.
    """
    for i in range(len(array)):
        if array[i] < 10:
            array[i] = 0
        elif array[i] > 20:
            array[i] = 1
    return array


def main():
    """
    Основная функция.
    """
    array = [5, 15, 25, 8, 22, 10, 3, 30, 12, 18, 7, 21, 14, 9, 11]
    print(f"Исходный массив: {array}")
    transformed_array = transform_array(array)
    print(f"Преобразованный массив: {transformed_array}")


if __name__ == "__main__":
    main()