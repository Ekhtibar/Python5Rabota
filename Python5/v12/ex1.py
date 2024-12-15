def find_smallest_odd_element(array):
    """
    Находит наименьший нечетный элемент списка.

    Args:
        array: Список целых чисел.

    Returns:
        Наименьший нечетный элемент или сообщение, если таких нет.
    """
    odd_elements = [x for x in array if x % 2 != 0]
    
    if odd_elements:
        return min(odd_elements)
    else:
        return "Нет нечетных элементов."


def main():
    """
    Основная функция.
    """
    array = [2, 4, 6, 8, 1, 3, 5, 7, 9, 11]
    smallest_odd = find_smallest_odd_element(array)
    print(f"Исходный массив: {array}")
    print(f"Наименьший нечетный элемент: {smallest_odd}")


if __name__ == "__main__":
    main()