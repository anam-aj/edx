#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.current_max_value = float('-inf')
        self.previous_max_values = []

    def Push(self, a):
        self.__stack.append(a)
        if a >= self.current_max_value:
            self.current_max_value = a
            self.previous_max_values.append(a)

    def Pop(self):
        assert(len(self.__stack))
        popped_value = self.__stack.pop()
        if not self.__stack:
            self.current_max_value = float('-inf')
            self.previous_max_values = []
        elif popped_value == self.current_max_value:
            self.previous_max_values.pop()
            self.current_max_value = self.previous_max_values[-1]

    def Max(self):
        assert(len(self.__stack))
        return self.current_max_value


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
