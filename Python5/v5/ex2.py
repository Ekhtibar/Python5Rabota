def remove_duplicates(array):
    """
    Удаляет дубликаты из массива, оставляя только уникальные элементы.

    Args:
        array: Массив целых чисел.

    Returns:
        Новый массив с уникальными элементами.
    """
    return list(set(array))


def main():
    """
    Основная функция.
    """
    array = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7]
    unique_array = remove_duplicates(array)
    print(f"Исходный массив: {array}")
    print(f"Массив с уникальными элементами: {unique_array}")


if __name__ == "__main__":
    main()