class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        if n > (self.capacity - self.size):
            raise ValueError
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
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
    def size(self, size):
        if not (int(size) >= 0) or not (int(size) % 1 == 0):
            raise ValueError
        self._size = size


def main():

    my_jar = Jar(15)
    print(my_jar)
    my_jar.deposit(3)
    print(my_jar)
    my_jar.withdraw(2)
    print(my_jar)
    my_jar.deposit(5)
    print(my_jar)


if __name__ == "__main__":
    main()
