# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    for i in range(len(data)):

    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def shift_down(index, array):

    if index == 0:
        parent = 0
    elif index % 2 == 0:
        parent = (index // 2) - 1
    else:
        parent = index //

    left_child = 2 * index + 1
    right_child = 2 * index + 2
    min_index = index

    if left_child < len(array) and array[left_child] < array[min_index]:
        min_index = left_child
    if right_child < len(array) and array[right_child] < array[min_index]:
        min_index = right_child

    array[index], array[min_index] = array[min_index], array[index]
    












def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
