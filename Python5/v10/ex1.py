def check_duplicates(array):
    """
    Проверяет, есть ли в массиве повторяющиеся элементы.

    Args:
        array: Массив чисел.

    Returns:
        Количество повторяющихся элементов или сообщение об их отсутствии.
    """
    duplicates = set()
    for item in array:
        if array.count(item) > 1:
            duplicates.add(item)
    
    if duplicates:
        return len(duplicates)
    else:
        return "Повторяющихся элементов нет."


def main():
    """
    Основная функция.
    """
    array = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9]
    result = check_duplicates(array)
    print(f"Исходный массив: {array}")
    print(f"Количество повторяющихся элементов: {result}")


if __name__ == "__main__":
    main()