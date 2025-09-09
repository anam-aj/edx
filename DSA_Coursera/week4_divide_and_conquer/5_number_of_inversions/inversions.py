from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0

    sorted_array, number_of_inversions = mergesort(a, number_of_inversions)

    return number_of_inversions


def mergesort(array, inversion):

    length = len(array)

    if length == 1:
        return array, inversion

    mid = length // 2

    left, inv_l = mergesort(array[:mid], inversion)
    right, inv_r = mergesort(array[mid:length], inv_l)

    sorted_array, inv_s = merge(left, right, inv_r)

    return sorted_array, inv_s


def merge(arr1, arr2, inversion):

    merged_arr = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        element_1, element_2 = arr1[i], arr2[j]

        if element_1 <= element_2:
            merged_arr.append(element_1)
            i += 1
        else:
            merged_arr.append(element_2)
            j += 1
            inversion += len(arr1) - i

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr, inversion


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
