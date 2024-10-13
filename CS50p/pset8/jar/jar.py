class Jar:
    def __init__(self, capacity=12):
        if not (capacity > 0) or (capacity % 1 != 0):
            raise ValueError
        self.capacity = capacity

    def __str__(self):
        return("abcd")

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):


def main():
    my_jar = Jar(10)
    print(my_jar)


if __name__ == "__main__":
    main()
