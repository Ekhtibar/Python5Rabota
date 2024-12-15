def sum_and_product(array):
    """
    Находит сумму элементов с четными номерами и произведение элементов с нечетными номерами.

    Args:
        array: Массив целых чисел.

    Returns:
        Кортеж (сумма четных, произведение нечетных).
    """
    even_sum = sum(array[i] for i in range(0, len(array), 2))
    odd_product = 1
    for i in range(1, len(array), 2):
        odd_product *= array[i]
    
    return even_sum, odd_product


def main():
    """
    Основная функция.
    """
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_sum, odd_product = sum_and_product(array)
    print(f"Исходный массив: {array}")
    print(f"Сумма элементов с четными номерами: {even_sum}")
    print(f"Произведение элементов с нечетными номерами: {odd_product}")


if __name__ == "__main__":
    main()