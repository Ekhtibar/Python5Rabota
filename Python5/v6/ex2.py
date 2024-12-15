def sum_greater_than_five(array):
    """
    Вычисляет сумму элементов массива, которые больше 5.

    Args:
        array: Массив целых чисел.

    Returns:
        Сумма элементов больше 5.
    """
    return sum(x for x in array if x > 5)


def main():
    """
    Основная функция.
    """
    array = []
    print("Введите 10 целых чисел:")
    for _ in range(10):
        number = int(input())
        array.append(number)

    total_sum = sum_greater_than_five(array)
    print(f"Исходный массив: {array}")
    print(f"Сумма чисел больше 5: {total_sum}")


if __name__ == "__main__":
    main()