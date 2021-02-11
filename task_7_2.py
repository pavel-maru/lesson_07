
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50).
#  Выведите на экран исходный и отсортированный массивы.

from random import uniform

def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    sep = len(lst) // 2
    left = merge_sort(lst[:sep])
    right = merge_sort(lst[sep:])
    # print(left, right)

    i = j = 0
    res_lst = []

    while i < len(left) or j < len(right):
        if i >= len(left):
            res_lst.append(right[j])
            j += 1
        elif j >= len(right):
            res_lst.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res_lst.append(left[i])
            i += 1
        else:
            res_lst.append(right[j])
            j += 1
        # print(res)

    return res_lst

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 50
lst = [round(uniform(MIN_ITEM, MAX_ITEM), 1) for _ in range(SIZE)]

print(lst)
print(merge_sort(lst))
# print(lst)
