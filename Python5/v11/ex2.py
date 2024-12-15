def get_even_less_than_ten(array):
    """
    Получает массив, состоящий только из четных чисел меньше 10.

    Args:
        array: Массив целых чисел.

    Returns:
        Новый массив четных чисел меньше 10 или сообщение, если таких нет.
    """
    even_numbers = [x for x in array if x % 2 == 0 and x < 10]
    
    if even_numbers:
        return sorted(even_numbers)  # Сортируем массив в порядке возрастания
    else:
        return "Нет четных чисел меньше 10."


def main():
    """
    Основная функция.
    """
    array = [12, 3, 4, 8, 1, 6, 10, 2, 5, 7]
    result = get_even_less_than_ten(array)
    print(f"Исходный массив: {array}")
    print(f"Четные числа меньше 10: {result}")


if __name__ == "__main__":
    main()