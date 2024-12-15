def find_min_by_absolute_and_reverse(array):
    """
    Находит минимальный по модулю элемент и выводит массив в обратном порядке.

    Args:
        array: Массив вещественных чисел.

    Returns:
        Минимальный по модулю элемент и массив в обратном порядке.
    """
    min_element = min(array, key=abs)  # Находим минимальный по модулю элемент
    reversed_array = array[::-1]  # Переворачиваем массив
    return min_element, reversed_array


def main():
    """
    Основная функция.
    """
    array = []
    print("Введите 10 вещественных чисел:")
    for _ in range(10):
        number = float(input())
        array.append(number)

    min_element, reversed_array = find_min_by_absolute_and_reverse(array)
    print(f"Минимальный по модулю элемент: {min_element}")
    print(f"Массив в обратном порядке: {reversed_array}")


if __name__ == "__main__":
    main()