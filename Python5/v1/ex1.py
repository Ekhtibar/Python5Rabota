def find_max_and_reverse(n):
  """
  Находит максимальный элемент в массиве и выводит массив в обратном порядке.

  Args:
    n: Длина массива.

  Returns:
    Максимальный элемент в массиве.
  """
  a = []
  for i in range(n):
    print(f"Введите {i} элемент: ")
    a.append(int(input()))

  max_element = max(a)
  print(f"Исходный массив: {a}")
  print(f"Максимальный элемент: {max_element}")
  print(f"Массив в обратном порядке: {a[::-1]}")

  return max_element

n = int(input("Введите длину массива: "))
find_max_and_reverse(n)