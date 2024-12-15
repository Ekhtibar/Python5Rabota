def count_even_odd(array):
    """
    Считает количество четных и нечетных элементов в массиве.

    Args:
        array: Массив чисел.

    Returns:
        Кортеж (количество четных, количество нечетных).
    """
    even_count = sum(1 for x in array if x % 2 == 0)
    odd_count = sum(1 for x in array if x % 2 != 0)
    return even_count, odd_count


def main():
    """
    Основная функция.
    """
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    even_count, odd_count = count_even_odd(array)
    print(f"Исходный массив: {array}")
    print(f"Количество четных элементов: {even_count}, Количество нечетных элементов: {odd_count}")


if __name__ == "__main__":
    main()