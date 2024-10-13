class Jar:
    def __init__(self, capacity=12, size):
        if not (int(capacity) > 0) or not (int(capacity) % 1 == 0):
            raise ValueError
        self.capacity = capacity

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
    def 

    @property
    def size(self):
        ...



def main():

    my_jar = Jar("a")
    print(my_jar.capacity)
    print(my_jar)


if __name__ == "__main__":
    main()
