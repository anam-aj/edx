from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):

    point_sorted_by_x = mergesort(points)
    min_distance_squared = float("inf")
    d = shortest_distance(points_sorted_by_x)

    '''for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))'''

    for p in points:
        ...

    return min_distance_squared

def shortest_distance(sorted_points):

    start = 0
    end = len(sorted_points) - 1

    index -1 



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
