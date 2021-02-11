
# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных;
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randrange

def sort_arr(array):
     array = array.copy()
     # print(len(array))
     for n in range(1, len(array)):
          for i in range(len(array) - n):
               if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    # print(array)
     return (array)

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
print(sort_arr(array))
