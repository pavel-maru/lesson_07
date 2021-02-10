
#  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#  в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint

MIN_ITEM = 0
MAX_ITEM = 1_000
m = int(input('Введите натуральное число: '))
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * m + 1)]
print(array)

for item in array:
    less = 0
    more = 0
    equal = 0
    for el in array:
        if el < item:
            less += 1
            # print(item, el, less)
        elif el > item:
            more += 1
            # print(item, el, more)
        else:
            equal += 1
            # print(item, el, equal)
        # print(less, equal, more)
    if abs(less - more) < equal:
        # print(abs(less - more), equal)
        # num = item
        break

# print(num)
print(item)
