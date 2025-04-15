import time

def insertion_Sort(list1):

    n = len(list1)
    for i in range(1, n):
        print(i)
        for j in range(i-1, -1, -1):
            print(numList)
            if list1[i] < list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
                i = j

numList = [55, 3, -2, -0.01, -3, 0.02, -7,]

insertion_Sort(numList)

print(numList)
