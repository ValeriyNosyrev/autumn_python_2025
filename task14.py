def find_min_distances(arr):
    index_list = []

    # Проходим по массиву и заполняем список индексов для каждого числа
    for i in range(len(arr)):
        num = arr[i]
        found = False
        for j in range(len(index_list)):
            if index_list[j][0] == num:
                index_list[j][1].append(i)
                found = True
                break
        if not found:
            index_list.append([num, [i]])

# Теперь ищем минимальные расстояния
    result = []
    for num, indices in index_list:
        if len(indices) < 2:
            result.append((num, None))
        else:
            min_dist = float('inf')
            closest_pair = None
# Ищем минимальное расстояние между соседними индексами
            for j in range(len(indices) - 1):
                idx1 = indices[j]
                idx2 = indices[j + 1]
                dist = idx2 - idx1
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (idx1, idx2)
            result.append((num, closest_pair))

    return result


# Пример использования
mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
result = find_min_distances(mass)

for num, pair in result:
    if pair is None:
        print(f"Для числа {num} нет минимального расстояния т.к. элемент в массиве один.")
    else:
        idx1, idx2 = pair
        print(f"Для числа {num} минимальное расстояние в массиве по индексам: {idx1} и {idx2}")