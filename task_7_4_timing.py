
from random import randint
import timeit

# вариант без индексов и с коротким if
def mediana(array):

    for item in array:
        less = more = equal = 0
        for el in array:
            if el < item:
                less += 1
            elif el > item:
                more += 1
            else:
                equal += 1
        if abs(less - more) < equal:
            return item

# вариант с индексами и длинным if
def median_square(array):
    for i in range(len(array)):
        smaller = equal = bigger = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                smaller += 1
            elif array[i] > array[j]:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or bigger == equal + smaller or \
                (equal > 1 and abs(bigger - smaller) < equal):
            return array[i]

# вариант с индексами и коротким if
def median_1(array):
    for i in range(len(array)):
        smaller = equal = bigger = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                smaller += 1
            elif array[i] > array[j]:
                bigger += 1
            else:
                equal += 1
        equal -= 1
        if abs(bigger - smaller) <= equal:
            return array[i]

# вариант с элементами и длинным if
def median_2(array):
    for number in array:
        smaller = equal = bigger = 0
        for num in array:
            if number < num:
                smaller += 1
            elif number > num:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or bigger == equal + smaller or \
                (equal > 1 and abs(bigger - smaller) < equal):
            return number



MIN_ITEM = -100
MAX_ITEM = 100
m = int(input('Введите натуральное число: '))
arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * m + 1)]

print(arr)
print(f'{mediana(arr)=}')

print(timeit.timeit('mediana(arr)', number=100, globals=globals()))

# вариант без индексов и с коротким if (Павла Марутенкова)
# m = 9: 0.0010401999999998246
# m = 99: 0.12742629999999977
# m = 999: 12.508164500000001

print(arr)
print(f'{median_square(arr)=}')

print(timeit.timeit('median_square(arr)', number=100, globals=globals()))

# вариант с индексами и длинным if (Алексея Петренко)
# m = 9: 0.002638999999999836
# m = 99: 0.2915472999999995
# m = 999: 24.9889439

print(arr)
print(f'{median_1(arr)=}')

print(timeit.timeit('median_1(arr)', number=100, globals=globals()))

# вариант с индексами и коротким if
# m = 9: 0.0026790999999999343
# m = 99: 0.43278940000000077
# m = 999: 25.676121800000004

print(arr)
print(f'{median_2(arr)=}')

print(timeit.timeit('median_2(arr)', number=100, globals=globals()))

# вариант с элементами и длинным if
# m = 9: 0.0011459999999998693
# m = 99: 0.13981719999999953
# m = 999: 12.243328000000005