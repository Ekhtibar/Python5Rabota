def replace_elements_less_than_15(array):
  """
  Заменяет элементы массива, меньшие 15, их удвоенными значениями.

  Args:
    array: Массив чисел.

  Returns:
    Преобразованный массив.
  """
  for i in range(len(array)):
    if array[i] < 15:
      array[i] = array[i] * 2
  return array


def main():
  """
  Основная функция.
  """
  array = [1, 2, 3, 4, 5, 6, 7, 8]
  transformed_array = replace_elements_less_than_15(array)
  print(f"Исходный массив: {array}")
  print(f"Преобразованный массив: {transformed_array}")


if __name__ == "__main__":
  main()