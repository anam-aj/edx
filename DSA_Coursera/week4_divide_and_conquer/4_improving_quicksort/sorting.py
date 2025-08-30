from random import randint


def randomized_quick_sort(elements, l, r):

    if l >= r:
        return

    index1, index2 = partition3(elements, l, r)

    randomized_quick_sort(elements, l, index1 - 1)
    randomized_quick_sort(elements, index2 + 1 , r)


def partition3(elements, l, r):

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

'''def partition3(array, left, right):
    # write your code here


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)'''


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
