class Jar:
    def __init__(self, capacity=12, size):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return("🍪" * size)

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

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
        self.size = size

def main():

    my_jar = Jar("a")
    print(my_jar.capacity)
    print(my_jar)


if __name__ == "__main__":
    main()
