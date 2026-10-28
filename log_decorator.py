def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула {result}")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(2, 3)
