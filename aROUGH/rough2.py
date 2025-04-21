def binary_search(sorted_list, key):

    first_index = 0
    if len(sorted_list) > 0:
        last_index = len(sorted_list) - 1
    else:
        return "empty list"

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if sorted_list[mid_index] == key:
            return mid_index
        elif sorted_list[mid_index] > key:
            last_index = mid_index - 1
        elif sorted_list[mid_index] < key:
            first_index = mid_index + 1

    return "key not found"


numList = sorted([1, 1, 2, 13.2, -11.1, 1, -3, 0])
key = 13.2
print(numList)
search_result = binary_search(numList, key)

if search_result == "empty list" or search_result == "key not found":
    print(search_result)
else:
    print(f"{key} is present at position number {search_result + 1}" )


test_cases = [
    ([], 5),  # Empty list, key 5
    ([1], 1),  # Single element, key present
    ([10], 5),  # Single element, key not present
    ([1, 3, 5, 7, 9], 5),  # Key present in multiple elements
    ([2, 4, 6, 8, 10], 7),  # Key not present
    ([1, 2, 3, 4, 5], 1),  # Key is the first element
    ([1, 2, 3, 4, 5], 5),  # Key is the last element
    ([1, 2, 2, 3, 4], 2),  # Duplicate elements, key present
    ([1, 2, 2, 3, 4], 5),  # Duplicate elements, key not present
    ([10, 20, 30, 40, 50], 30),  # Larger numbers
]

# Iterate over the test cases and run binary_search for each
for sorted_list, key in test_cases:
    result = binary_search(sorted_list, key)
    print(f"List: {sorted_list}, Key: {key}")
    if result == "empty list" or result == "key not found":
        print(result)
    else:
        print(f"{key} is present at position number {result + 1}" )
