def binary_search(sortedList, ):
    n = len(list3)
    for i in range(n):
        temp = list3[i]
        j = i - 1
        while j >= 0 and temp < list3[j]:
            list3[j+1] = list3[j]
            j = j-1
        list3[j+1] = temp


numList = [1, 1, 2, 13.2, -11.1, 1, -3, 0]
insertion_Sort(numList)
print("The sorted list is :", numList)

