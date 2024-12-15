def find_duplicates(array):
    """
    Проверяет, есть ли в массиве повторяющиеся элементы и выводит их.

    Args:
        array: Массив целых чисел.

    Returns:
        Список повторяющихся элементов или сообщение об их отсутствии.
    """
    seen = set()
    duplicates = set()
    
    for item in array:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    if duplicates:
        return list(duplicates)
    else:
        return "Нет повторяющихся элементов."


def main():
    """
    Основная функция.
    """
    array = [1, 2, 3, 4, 1, 5, 6, 2]
    result = find_duplicates(array)
    print(f"Исходный массив: {array}")
    print(f"Повторяющиеся элементы: {result}")


if __name__ == "__main__":
    main()