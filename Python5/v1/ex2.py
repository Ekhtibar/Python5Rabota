def replace_zeros_with_average(n):
  """
  Заменяет нулевые элементы в массиве на среднее арифметическое.

  Args:
    n: Длина массива.
  """
  a = []
  for i in range(n):
    print(f"Введите {i} элемент: ")
    a.append(float(input()))

  sum_of_elements = sum(a)
  non_zero_count = len([x for x in a if x != 0])
  average = sum_of_elements / non_zero_count if non_zero_count else 0

  for i in range(n):
    if a[i] == 0:
      a[i] = average

  print(f"Исходный массив: {a}")
  print(f"Массив с замененными нулями: {a}")

n = int(input("Введите длину массива: "))
replace_zeros_with_average(n)