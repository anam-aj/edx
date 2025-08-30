import random

def randomized_quick_sort(elements, l, r):

    if l >= r:
        return

    index1, index2 = partition3(elements, l, r)

    randomized_quick_sort(elements, l, index1 - 1)
    randomized_quick_sort(elements, index2 + 1 , r)


def partition3(elements, l, r):

    pivot = random.randint(l, r)
    elements[l], elements[pivot] = elements[pivot], elements[l]

    pivot = l
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


l = [2, 4, -1, -10]

#Already sorted list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Reverse sorted list
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]

#List with duplicates
l = [4, 2, 7, 2, 4, 9, 1, 2]

#Single element list
l = [5]

#Empty list
l = []

#All elements equal
l = [3, 3, 3, 3, 3]

#Random order (medium size)
l = [10, 3, 5, 8, 2, 7, 6, 1, 4, 9]

#Large range mixed
l = [100, -50, 200, 0, -10, 75, 150, -200]

l = [2, 3, 1, 1, 4, 10, 1, 7, 6, 1, 1, 22, -1, -1, 3, -10]



r = len(l) - 1
randomized_quick_sort(l, 0, r)
print(l)

failures = []
for _ in range(5000):  # test 5000 random arrays
    size = random.randint(0, 12)
    arr = [random.randint(-5, 5) for _ in range(size)]
    copy = arr.copy()
    if copy:
        randomized_quick_sort(copy, 0, len(copy)-1)
    if copy != sorted(arr):
        failures.append((arr, copy, sorted(arr)))

print("Number of failures:", len(failures))
if failures:
    print("Examples:", failures[:5])
