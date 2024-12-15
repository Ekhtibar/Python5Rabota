def find_min_and_display(n):
    """
    Находит минимальный элемент в массиве и выводит массив в прямом порядке.

    Args:
        n: Длина массива.

    Returns:
        Минимальный элемент в массиве.
    """
    a = []
    for i in range(n):
        print(f"Введите {i} элемент: ")
        a.append(int(input()))

    min_element = min(a)
    print(f"Исходный массив: {a}")
    print(f"Минимальный элемент: {min_element}")

    return min_element

n = int(input("Введите длину массива: "))
find_min_and_display(n)