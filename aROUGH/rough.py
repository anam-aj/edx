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


def search_index_ends(keys, query):
    # write your code here

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


l = [ 1.1,1.4,1.5,1.6,2,2,3,3,3,3,3,4,4,4,5,5,6,6]
k = [ 0  ,1  ,2  ,3  ,4,5,6,7,8,9,0,1,2,3,4,5,6,7]


print(search_index_ends(l,3))
