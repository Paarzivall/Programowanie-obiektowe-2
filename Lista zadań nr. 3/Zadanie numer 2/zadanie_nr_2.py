def gen_calkowite():
    i = 0
    while True:
        yield i
        i += 1


def gen_kwadrat(x):
    yield x * x


def select():
    tab = []


def main():
    for i in gen_calkowite():
        for x in gen_kwadrat(i):
            print(f"Kwadrat liczby: {i} wynosi: {x}")


if __name__ == '__main__':
    main()
