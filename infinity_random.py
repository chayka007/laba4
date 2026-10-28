import random


def infinite_random(lower, upper):
    while True:
        yield random.randint(lower, upper)


if __name__ == "__main__":
    generator = infinite_random(1, 6)
    values = [next(generator) for _ in range(10)]
    print(values)
