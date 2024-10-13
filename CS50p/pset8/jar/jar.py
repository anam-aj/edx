class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return("🍪" * self.size)

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not (int(capacity) > 0) or not (int(capacity) % 1 == 0):
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def capacity(self, size):
        if not (int(size) > 0) or not (int(size) % 1 == 0):
            raise ValueError
        self._size = size


def main():

    my_jar = Jar(15, 10)
    print(my_jar)


if __name__ == "__main__":
    main()
