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


# Пример использования
if __name__ == "__main__":
    # Ввод размера массива и его элементов

    N = int(input("Введите размер массива: "))
    A = []
    print("Введите элементы массива.")

    for i in range(N):
        print(f"Элемент {i+1} из {N} :")
        A.append(int(input()))

    result = find_sum_of_negatives_between_max_min(A)
    print(
        f"Сумма отрицательных элементов между "
        f"максимальным и минимальным: {result}")
