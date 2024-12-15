def swap_arrays(array_a, array_b):
    """
    Меняет местами содержимое массивов A и B.

    Args:
        array_a: Массив A.
        array_b: Массив B.

    Returns:
        Преобразованные массивы A и B.
    """
    return array_b, array_a  # Меняем местами массивы


def main():
    """
    Основная функция.
    """
    array_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array_b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(f"Исходный массив A: {array_a}")
    print(f"Исходный массив B: {array_b}")

    array_a, array_b = swap_arrays(array_a, array_b)

    print(f"Преобразованный массив A: {array_a}")
    print(f"Преобразованный массив B: {array_b}")


if __name__ == "__main__":
    main()