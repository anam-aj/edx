# python3

import sys
import threading


def compute_height(n, parents):

    child_list = []
    for _ in range(n):
        child_list.append([])

    for i, parent in enumerate(parents):
        if parent == -1:
            root_node = i
        else:
            child_list[parent].append(i)

    '''def height(node):
        if not child_list[node]:
            return 1
        return 1 + max(height(child) for child in child_list[node])

    return height(root_node)'''

    depth = 0
    queue = []
    queue.append(child_list[root_node])
    depth[root_node] += 1
    while queue:
        curr_node_child = queue.pop(0)
        for child in curr_node_child:
            depth[child] = depth[root_node] + 1
            queue.append(child_list[child])

    return (max(heights))


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
