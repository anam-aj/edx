def binary_search_duplicate(keys, query):
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

l = [-1,1,1,1,2,2,3,3,3,3,3,4,4,4,5,5,6,6]
k = [ 0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7]

print(binary_search_duplicate(l, 6))
