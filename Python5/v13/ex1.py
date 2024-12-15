def find_duplicates(array):
    """
    Проверяет, есть ли в массиве одинаковые элементы и выводит их индексы.

    Args:
        array: Массив целых чисел.

    Returns:
        Словарь с элементами и их индексами или сообщение об отсутствии дубликатов.
    """
    duplicates = {}
    for index, value in enumerate(array):
        if array.count(value) > 1:
            if value not in duplicates:
                duplicates[value] = []
            duplicates[value].append(index)
    
    if duplicates:
        return duplicates
    else:
        return "Нет одинаковых элементов."


def main():
    """
    Основная функция.
    """
    array = [1, 2, 3, 4, 1, 5, 6, 2]
    result = find_duplicates(array)
    print(f"Исходный массив: {array}")
    print(f"Дубликаты и их индексы: {result}")


if __name__ == "__main__":
    main()