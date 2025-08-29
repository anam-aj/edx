def quick_sort(elements, l, r):

    if l >= r:
        return

    index1, index2 = partition(elements, l, r)

    quick_sort(elements, l, index1 - 1)
    quick_sort(elements, index2 + 1 , r)


def partition(elements, l, r):

    pivot = elements[l]
    j = l

    for i in range(l + 1, r + 1):
        if elements[i] > pivot:
            pass
        elif elements[i] <= pivot:
            tmp = elements[j + 1]
            elements[j + 1] = elements[i]
            elements[i] = tmp
            j += 1

    tmp = elements[l]
    elements[l] = elements[j]
    elements[j] = tmp

    return j


l = [2, 3, 1, 1, 4, 10, 1, 7, 6, 1, 1]
r = len(l) - 1
quick_sort(l, 0, r)
print(l)
