
from random import randint
import timeit
# from matplotlib import pyplot as plt

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

m_list = [n for n in range(100, 1000, 100)]
MIN_ITEM = 0
MAX_ITEM_1 = 10

res1 = []
# res2 = []
# res3 = []
res4 = []

for m in m_list:
    arr = [randint(MIN_ITEM, MAX_ITEM_1) for _ in range(2 * m + 1)]
    res1.append(round(timeit.timeit('mediana(arr)', number=10, globals=globals()), 4))
    res4.append(round(timeit.timeit('median_2(arr)', number=10, globals=globals()), 4))

print(f'var 1 (el + short if):\t{res1}, '
      f'\nvar 4 (el + long if):\t{res4}')
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.plot(m_list, res)
# ax.grid(True)

MIN_ITEM = 0
MAX_ITEM_1 = 10_000

res1 = []
res4 = []

for m in m_list:
    arr = list({randint(MIN_ITEM, MAX_ITEM_1) for _ in range(2 * m + 1)})
    res1.append(round(timeit.timeit('mediana(arr)', number=10, globals=globals()), 4))
    res4.append(round(timeit.timeit('median_2(arr)', number=10, globals=globals()), 4))

print(f'var 1 (el + short if):\t{res1}, '
      # f'\nvar 2 (ind + long if):\t{res2}, '
      # f'\nvar 3 (ind + short if):\t{res3}, '
      f'\nvar 4 (el + long if):\t{res4}')


# Много повторяющихся элементов (MIN = 0, MAX = 10)
# var 1 (el + short if):	[0.0061, 0.0113, 0.0093, 0.012, 0.0173, 0.0234, 0.0392, 0.0094, 0.0112],
# var 4 (el + long if):	    [0.0043, 0.0135, 0.0081, 0.0107, 0.0169, 0.0238, 0.0559, 0.0078, 0.0097]

# Все элементы уникальны (MIN = 0, MAX = 10_000)
# var 1 (el + short if):	[0.0526, 0.2751, 0.2174, 1.1256, 1.796, 2.4598, 3.5006, 3.0472, 5.2847],
# var 4 (el + long if):	    [0.0528, 0.2924, 0.2081, 1.111, 1.748, 2.4504, 3.4267, 2.885, 5.5295]
