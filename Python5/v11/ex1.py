def find_largest_even_element(array):
    """
    Находит наибольший элемент списка, который делится на 2 без остатка.

    Args:
        array: Список целых чисел.

    Returns:
        Наибольший четный элемент или сообщение, если таких нет.
    """
    even_elements = [x for x in array if x % 2 == 0]
    
    if even_elements:
        return max(even_elements)
    else:
        return "Нет четных элементов."


def main():
    """
    Основная функция.
    """
    array = [1, 3, 5, 7, 2, 4, 6, 8, 10, 12]
    largest_even = find_largest_even_element(array)
    print(f"Исходный массив: {array}")
    print(f"Наибольший четный элемент: {largest_even}")


if __name__ == "__main__":
    main()