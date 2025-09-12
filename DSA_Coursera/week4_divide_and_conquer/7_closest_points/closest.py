from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance(sorted_points_by_x):

    '''for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))'''

    min_distance_squared = float("inf")

    if len(sorted_points_by_x) <= 3:
        for p, q in combinations(sorted_points_by_x, 2):
            min_distance_squared = min(min_distance_squared, distance_squared(p, q))
            min_dist = sqrt(min_distance_squared)

        return min_dist

    length = len(sorted_points_by_x)
    mid = length // 2
    d1 = minimum_distance(sorted_points_by_x[:mid])
    d2 = minimum_distance(sorted_points_by_x[mid:length])

    d = min(d1, d2)
    strip_points = strip(sorted_points_by_x, d, sorted_points_by_x[mid].x)



def strip(sorted_points_by_x, d, mid_x):

    min_x = mid_x - d
    max_x = mid_x + d

    min_index = search_index_starts(sorted_points_by_x, min_x)




def search_index_starts(sorted_points_by_x, min_x):

    start = 0
    end = len(sorted_points_by_x) - 1

    index = -1

    while end >= start:
        mid = (end + start) // 2

        if sorted_points_by_x[mid].x <= min_x:
            index = mid
            start = mid + 1
        else:
            end = mid - 1

    return index


def search_index_ends(keys, query):

    start = 0
    end = len(keys) - 1

    index = -1

    while end >= start:
        mid = (end + start) // 2

        if keys[mid] < query:
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


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
