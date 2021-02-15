
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

m_list = [n for n in range(100, 2000, 100)]
MIN_ITEM = 0
MAX_ITEM = 100

# вариант без индексов и с коротким if (Павла Марутенкова)

res1 = []
res2 = []
res3 = []
res4 = []

for m in m_list:
    arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * m + 1)]
    res1.append(round(timeit.timeit('mediana(arr)', number=10, globals=globals()), 4))
    res2.append(round(timeit.timeit('median_square(arr)', number=10, globals=globals()), 4))
    res3.append(round(timeit.timeit('median_1(arr)', number=10, globals=globals()), 4))
    res4.append(round(timeit.timeit('median_2(arr)', number=10, globals=globals()), 4))

print(f'var 1 (el + short if):\t{res1}, '
      f'\nvar 2 (ind + long if):\t{res2}, '
      f'\nvar 3 (ind + short if):\t{res3}, '
      f'\nvar 4 (el + long if):\t{res4}')
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.plot(m_list, res)
# ax.grid(True)
#
# var 1 (el + short if):	[0.018, 0.0115, 0.0832, 0.1276, 0.0177, 0.1241, 0.1524, 0.1541, 0.3955, 0.177, 0.3897, 0.0194, 0.0895, 1.4408, 0.2885, 0.6497, 0.5287, 1.1341, 0.2177],
# var 2 (ind + long if):	[0.0376, 0.028, 0.1479, 0.2546, 0.0436, 0.2601, 0.2715, 0.3757, 0.7332, 0.3472, 0.7419, 0.0405, 0.1735, 2.9472, 0.5731, 1.3953, 1.1888, 2.3493, 0.5394],
# var 3 (ind + short if):	[0.0377, 0.0268, 0.1613, 0.2686, 0.0417, 0.2708, 0.2935, 0.3365, 0.7657, 0.3796, 0.7597, 0.0435, 0.1899, 3.3686, 0.6033, 1.4587, 1.1662, 2.5804, 0.5559],
# var 4 (el + long if):	    [0.0187, 0.0115, 0.0543, 0.142, 0.0181, 0.1106, 0.1318, 0.1469, 0.3869, 0.1747, 0.3469, 0.0176, 0.0712, 1.3765, 0.2799, 0.6655, 0.5295, 1.1402, 0.251]
