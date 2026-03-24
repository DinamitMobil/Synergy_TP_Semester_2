def find_sum_of_negatives_between_max_min(arr):
    if len(arr) < 2:
        return 0  # Если меньше 2 элементов, между max и min ничего нет

    # Находим индексы максимального и минимального элементов
    max_idx = arr.index(max(arr))
    min_idx = arr.index(min(arr))

    # Определяем границы отрезка: от меньшего индекса к большему
    start = min(max_idx, min_idx)
    end = max(max_idx, min_idx)

    # Суммируем отрицательные элементы между start и end
    subsegment = arr[start:end + 1]

    result_sum = sum(x for x in subsegment if x < 0)

    return result_sum


def entering_array_size():
    # Обработка исключений ввода размера массива
    while True:
        try:
            input_result = int(input("Введите размер массива: "))
            if input_result > 1:
                break
            else:
                print("Значение должно быть больше 1.")
        except ValueError:
            print("Значение может быть только целым числом.")
    return input_result


def entering_array_element(size, element_number):
    # Обработка исключений ввода элементов массива
    while True:
        try:
            input_result = int(
                input(f"Элемент {element_number + 1} из {size} :"))
            break
        except ValueError:
            print("Значение может быть только целым числом.")
    return input_result


# Пример использования
if __name__ == "__main__":

    # Ввод размера массива
    size_array = entering_array_size()
    elements = []
    print("Введите элементы массива.")

    for i in range(size_array):
        # Ввод элементов массива
        elements.append(entering_array_element(size_array, i))

    # Обработка полученного массива
    result = find_sum_of_negatives_between_max_min(elements)

    # Выводим результат
    print(
        f"Сумма отрицательных элементов между "
        f"максимальным и минимальным: {result}")
