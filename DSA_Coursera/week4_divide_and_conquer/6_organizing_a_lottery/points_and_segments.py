from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    '''for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1'''

    sorted_starts = mergesort(starts)
    sorted_ends = mergesort(ends)


    for index, point in enumerate(points):
        lesser_starts = search_index(sorted_starts, point)
        lesser_ends = search_index(sorted_ends, point)
        

    return count


def search_index(keys, query):
    # write your code here

    start = 0
    end = len(keys) - 1

    index = -1

    while end >= start:
        mid = (end + start) // 2

        if keys[mid] <= query:
            index = mid
            start = mid + 1
        else:
            end = mid - 1

    return index


def mergesort(array):

    length = len(array)

    if length == 1:
        return array

    mid = length // 2

    left = mergesort(array[:mid])
    right = mergesort(array[mid:length])

    sorted_array = merge(left, right)

    return sorted_array


def merge(arr1, arr2):

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

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
