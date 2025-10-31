import random


def majority_element_naive(elements):
    randomized_quick_sort(elements, 0, len(elements) - 1)

    n = len(elements)
    half = n // 2

    if n % 2 == 0:
        for i in range(half):
            if elements[i] == elements[i + half]:
                return 1
    else:
        for i in range(half + 1):
            if elements[i] == elements[i + half]:
                return 1

    return 0


def randomized_quick_sort(elements, l, r):

    if l >= r:
        return

    index1, index2 = partition3(elements, l, r)

    randomized_quick_sort(elements, l, index1 - 1)
    randomized_quick_sort(elements, index2 + 1 , r)


def partition3(elements, l, r):

    rand_pivot = random.randint(l, r)
    elements[l], elements[rand_pivot] = elements[rand_pivot], elements[l]

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


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
