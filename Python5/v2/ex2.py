def count_positive_negative(n):
    """
    Считает количество положительных и отрицательных элементов в массиве.

    Args:
        n: Длина массива.
    """
    a = []
    for i in range(n):
        print(f"Введите {i} элемент: ")
        a.append(int(input()))

    positive_count = len([x for x in a if x > 0])
    negative_count = len([x for x in a if x < 0])

    print(f"Исходный массив: {a}")
    print(f"Количество положительных элементов: {positive_count}")
    print(f"Количество отрицательных элементов: {negative_count}")

n = int(input("Введите длину массива: "))
count_positive_negative(n)