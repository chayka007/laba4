import random


def random_numbers(count, lower, upper):
    for _ in range(count):
        yield random.randint(lower, upper)


if __name__ == "__main__":
    print(list(random_numbers(5, 1, 100)))
