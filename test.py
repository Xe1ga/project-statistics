@test_func
def test_func_2(name: str):
    """

    :param name:
    :param count:
    :return:
    """
    s = f'Привет, {name}'
    return s

def test_func(text: str, count: int = 10):
    """

    :param text:
    :param count:
    :return:
    """
    for _ in range(count):
        print(text)
    print (f'Количество повторов: {count}.')


if __name__ == "__main__":
    test_func_2('Ольга Седова')
