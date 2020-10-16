
def test_func_2(count: int = 5):
    for _ in range(count):
        test_func('Привет')


def test_func(text: str, count: int = 10, fio: str):
    for _ in range(count):
        print(text, fio)


if __name__ == "__main__":
    test_func_2()
