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


"""import random
import time
import math

def check_complexity(merge_sort, sizes=[1000, 2000, 4000, 8000, 16000], trials=3):
    results = []

    for n in sizes:
        total_time = 0
        for _ in range(trials):
            arr = [random.randint(-100000, 100000) for _ in range(n)]
            start = time.time()
            merge_sort(arr.copy())
            total_time += time.time() - start
        avg_time = total_time / trials
        results.append((n, avg_time))
        print(f"n={n:<6} | time={avg_time:.6f}s")

    print("\n--- Growth Analysis ---")
    for i in range(1, len(results)):
        n1, t1 = results[i-1]
        n2, t2 = results[i]

        # Expected factor if O(n log n)
        expected = (n2 * math.log2(n2)) / (n1 * math.log2(n1))
        actual = t2 / t1 if t1 > 0 else float("inf")

        print(f"From n={n1} → n={n2} | "
              f"Expected growth ≈ {expected:.2f}x | "
              f"Actual growth ≈ {actual:.2f}x")

    print("\nIf 'Actual growth' is close to 'Expected growth', your algorithm is O(n log n).")

check_complexity(mergesort)"""
