def compare_with_max(array):
    """
    Находит максимальный элемент и считает количество меньших и больших элементов.

    Args:
        array: Массив целых чисел.

    Returns:
        Кортеж (количество меньших, количество равных, количество больших).
    """
    max_element = max(array)
    less_count = sum(1 for x in array if x < max_element)
    equal_count = sum(1 for x in array if x == max_element)
    greater_count = sum(1 for x in array if x > max_element)

    return less_count, equal_count, greater_count


def main():
    """
    Основная функция.
    """
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
    less, equal, greater = compare_with_max(array)
    print(f"Исходный массив: {array}")
    print(f"Количество меньших: {less}, Равных: {equal}, Больших: {greater}")


if __name__ == "__main__":
    main()