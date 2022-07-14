import timeit


def isEven_first(value):
    return value % 2 == 0


def isEven_second(value):
    return bin(value)[-1] == '0'


def main():
    time = 0
    for i in range(1, 10000, 5):
        time += timeit.timeit(lambda: isEven_first(i))
    print(f"first time: {time}")

    time = 0
    for i in range(1, 10000, 5):
        time += timeit.timeit(lambda: isEven_first(i))
    print(f"second time: {time}")


if __name__ == '__main__':
    main()


