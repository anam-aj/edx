class Jar:
    def __init__(self, capacity=12):
        if not (capacity > 0) or not (capacity % 1 == 0):
            raise ValueError
        self.capacity = capacity

    def __str__(self):
        return("abcd")


def main():

    my_jar = Jar(13)
    print(my_jar.capacity)
    print(my_jar)


if __name__ == "__main__":
    main()
