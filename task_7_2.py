
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50).
#  Выведите на экран исходный и отсортированный массивы.

from random import uniform

def merge_sort(array):

    if len(array) <= 1:
        return array

    sep = len(array) // 2
    left = merge_sort(array[:sep])
    right = merge_sort(array[sep:])
    # print(left, right)

    i = j = 0
    res_arr = []

    while i < len(left) or j < len(right):
        if i >= len(left):
            res_arr.append(right[j])
            j += 1
        elif j >= len(right):
            res_arr.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res_arr.append(left[i])
            i += 1
        else:
            res_arr.append(right[j])
            j += 1
        # print(res)

    return res_arr

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 50
array = [round(uniform(MIN_ITEM, MAX_ITEM), 1) for _ in range(SIZE)]

print(array)
print(merge_sort(array))
