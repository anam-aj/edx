def quick_sort(elements, l, r):

    if l > r:
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
            tmp_id1 = elements[index1]
            tmp = elements[index2 + 1]
            elements[index1] = elements[i]
            elements[index2 + 1] = tmp_id1
            elements[i] = tmp
            index1 += 1
            index2 += 1

    '''tmp = elements[l]
    elements[l] = elements[index1 - 1]
    elements[index1 - 1] = tmp
    index1 -= 1'''

    return (index1, index2)


l = [2, 3, 1, 1, 4, 10, 1, 7, 6, 1, 1, 22, -1, -1, 3, -10]
l = [2, 3, 1, 1, 4, 10, 1, 7, 6, 1, 1, 22, -1, -1, 3, -10]
r = len(l) - 1
quick_sort(l, 0, r)
print(l)
