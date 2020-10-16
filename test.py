
def test_func(text: str, count: int = 10):
    for _ in range(count):
        print(text)


if __name__ == "__main__":
    test_func('Привет')
