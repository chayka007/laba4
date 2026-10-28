from functools import reduce


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = reduce(lambda acc, x: acc + x, numbers)
    print(total)


if __name__ == "__main__":
    main()
