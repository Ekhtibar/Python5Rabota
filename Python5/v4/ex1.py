def find_max_element_and_index(array):
    """
    Находит максимальный элемент в массиве и его индекс.

    Args:
        array: Массив чисел.

    Returns:
        Кортеж (максимальный элемент, индекс).
    """
    max_element = max(array)
    max_index = array.index(max_element)
    return max_element, max_index


def main():
    """
    Основная функция.
    """
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    max_element, max_index = find_max_element_and_index(array)
    print(f"Исходный массив: {array}")
    print(f"Максимальный элемент: {max_element}, Индекс: {max_index}")


if __name__ == "__main__":
    main()