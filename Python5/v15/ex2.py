def get_odd_numbers(array):
    """
    Получает массив, состоящий только из нечетных чисел.

    Args:
        array: Массив целых чисел.

    Returns:
        Новый массив нечетных чисел или сообщение, если таких нет.
    """
    odd_numbers = [x for x in array if x % 2 != 0]
    
    if odd_numbers:
        return sorted(odd_numbers, reverse=True)  # Сортируем в порядке убывания
    else:
        return "Нет нечетных чисел."


def main():
    """
    Основная функция.
    """
    array = [10, 21, 32, 43, 54, 65, 76, 87, 98, 99]
    result = get_odd_numbers(array)
    print(f"Исходный массив: {array}")
    print(f"Нечетные числа: {result}")


if __name__ == "__main__":
    main()