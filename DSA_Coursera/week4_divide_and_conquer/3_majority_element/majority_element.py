def majority_element_naive(elements):
    quick_sort(elements, 0, len(elements) - 1)

    n = len(elements)
    mid = n // 2

    if n % 2 == 0:
        if elements[mid] == elements[0] or elements[mid - 1] == elements[-1]:
            return 1
        else:
            return 0
    else:
        if elements[mid] == elements[0] or elements[mid] == elements[-1]:
            return 1
        else:
            return 0


def quick_sort(elements, l, r):

    if l >= r:
        return

    index = partition(elements, l, r)

    quick_sort(elements, l, index - 1)
    quick_sort(elements, index + 1 , r)


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


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
