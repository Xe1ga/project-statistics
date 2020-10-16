
def test_func_2(name: str, count: int = 5):
    for _ in range(count):
        test_func(f'Привет, {name}')


def test_func(text: str, count: int = 10):
    print(text)


if __name__ == "__main__":
    test_func_2('Ольга')
