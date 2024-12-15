def swap_min_max(array):
    """
    Переставляет минимальный и максимальный элементы в массиве.

    Args:
        array: Массив целых чисел.

    Returns:
        Массив с переставленными минимальным и максимальным элементами.
    """
    min_index = array.index(min(array))
    max_index = array.index(max(array))
    
    # Перестановка
    array[min_index], array[max_index] = array[max_index], array[min_index]
    
    return array


def main():
    """
    Основная функция.
    """
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 0]
    swapped_array = swap_min_max(array)
    print(f"Исходный массив: {array}")
    print(f"Массив после перестановки минимального и максимального элементов: {swapped_array}")


if __name__ == "__main__":
    main()