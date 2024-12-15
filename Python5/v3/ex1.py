def calculate_sum_of_odd_elements(array):
  """
  Вычисляет сумму элементов массива с нечетными индексами.

  Args:
    array: Массив чисел.

  Returns:
    Сумму элементов массива с нечетными индексами.
  """
  sum = 0
  for i in range(1, len(array), 2):
    sum += array[i]
  return sum


def main():
  """
  Основная функция.
  """
  array_d = [1, 2, 3, 4, 5, 6, 7, 8]
  sum_of_odd_elements = calculate_sum_of_odd_elements(array_d)
  print(f"Массив D: {array_d}")
  print(f"Сумма элементов с нечетными индексами: {sum_of_odd_elements}")


if __name__ == "__main__":
  main()