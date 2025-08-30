import random

def quick_sort(elements, l, r):

    if l >= r:
        return

    index1, index2 = partition(elements, l, r)

    quick_sort(elements, l, index1 - 1)
    quick_sort(elements, index2 + 1 , r)


def partition(elements, l, r):

    pivot = elements[l]
    index1 = l
    index2 = l

    for i in range(l + 1, r + 1):
        if elements[i] > pivot:
            pass
        elif elements[i] == pivot:
            tmp = elements[index2 + 1]
            elements[index2 + 1] = elements[i]
            elements[i] = tmp
            index2 += 1
        elif elements[i] < pivot:
            tmp = elements[index1]
            elements[index1] = elements[i]
            elements[i] = tmp
            tmp = elements[index2 + 1]
            elements[index2 + 1] = elements[i]
            elements[i] = tmp
            index1 += 1
            index2 += 1

    return (index1, index2)


l = [-3, -1, 4, -3, 5]


r = len(l) - 1
quick_sort(l, 0, r)
print(l)

failures = []
for _ in range(5000):  # test 5000 random arrays
    size = random.randint(0, 12)
    arr = [random.randint(-5, 5) for _ in range(size)]
    copy = arr.copy()
    if copy:
        quick_sort(copy, 0, len(copy)-1)
    if copy != sorted(arr):
        failures.append((arr, copy, sorted(arr)))

print("Number of failures:", len(failures))
if failures:
    print("Examples:", failures[:5])
