from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    sorted_points_by_x = mergesort_x(points)
    #sorted_points_by_y = mergesort_y(points)

    dis = minimum_distance(sorted_points_by_x)

    return dis


def minimum_distance(sorted_points_by_x):

    min_distance_squared = float("inf")

    if len(sorted_points_by_x) <= 3:
        for p, q in combinations(sorted_points_by_x, 2):
            min_distance_squared = min(min_distance_squared, distance_squared(p, q))
            #min_dist = sqrt(min_distance_squared)

        return min_distance_squared

    length = len(sorted_points_by_x)
    mid = length // 2
    d1 = minimum_distance(sorted_points_by_x[:mid])
    d2 = minimum_distance(sorted_points_by_x[mid:length])

    min_distance_squared = min(d1, d2)
    strip_points = strip(sorted_points_by_x, sqrt(min_distance_squared), sorted_points_by_x[mid].x)
    strip_sorted_by_y = mergesort_y(strip_points)

    for i in range(len(strip_sorted_by_y)):
        for j in range(i + 1, min(i + 8, len(strip_sorted_by_y))):
            min_distance_squared = min(min_distance_squared, distance_squared(strip_sorted_by_y[i], strip_sorted_by_y[j]))

    return min_distance_squared


def strip(sorted_points_by_x, d, mid_x):

    min_x = mid_x - d
    max_x = mid_x + d

    min_index = search_index_starts(sorted_points_by_x, min_x)
    max_index = search_index_ends(sorted_points_by_x, max_x)

    if min_index == -1 or max_index == -1 or min_index > max_index:
        return []

    center_strip = sorted_points_by_x[min_index : max_index + 1]
    return center_strip


def search_index_starts(sorted_points_by_x, min_x):

    start = 0
    end = len(sorted_points_by_x) - 1

    index = -1

    while end >= start:
        mid = (end + start) // 2

        if sorted_points_by_x[mid].x >= min_x:
            index = mid
            end = mid - 1
        else:
            start = mid + 1

    return index


def search_index_ends(sorted_points_by_x, max_x):

    start = 0
    end = len(sorted_points_by_x) - 1

    index = -1

    while end >= start:
        mid = (end + start) // 2

        if sorted_points_by_x[mid].x <= max_x:
            index = mid
            start = mid + 1
        else:
            end = mid - 1

    return index


def mergesort_x(array):

    length = len(array)

    if length <= 1:
        return array

    mid = length // 2

    left = mergesort_x(array[:mid])
    right = mergesort_x(array[mid:length])

    sorted_array = merge_x(left, right)

    return sorted_array


def merge_x(arr1, arr2):

    merged_arr = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        element_1, element_2 = arr1[i], arr2[j]

        if element_1.x <= element_2.x:
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


def mergesort_y(array):

    length = len(array)

    if length <= 1:
        return array

    mid = length // 2

    left = mergesort_y(array[:mid])
    right = mergesort_y(array[mid:length])

    sorted_array = merge_y(left, right)

    return sorted_array


def merge_y(arr1, arr2):

    merged_arr = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        element_1, element_2 = arr1[i], arr2[j]

        if element_1.y <= element_2.y:
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
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
