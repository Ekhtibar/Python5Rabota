def swap_max_min(array):
    """
    Находит максимальный и минимальный элементы массива и меняет их местами.

    Args:
        array: Массив целых чисел.

    Returns:
        Массив с поменянными местами максимальным и минимальным элементами.
    """
    max_index = array.index(max(array))
    min_index = array.index(min(array))
    
    # Меняем местами
    array[max_index], array[min_index] = array[min_index], array[max_index]
    
    return array


def main():
    """
    Основная функция.
    """
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 0]
    print(f"Исходный массив: {array}")
    swapped_array = swap_max_min(array)
    print(f"Массив после замены максимального и минимального элементов: {swapped_array}")


if __name__ == "__main__":
    main()