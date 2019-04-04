def gen_calkowite():
    i = 0
    while True:
        yield i
        i += 1


def gen_kwadrat():
    for liczba in gen_calkowite():
        yield liczba ** 2


def select(obiekt, n):
    tab = []
    iterator = iter(obiekt)
    for x in range(n):
        try:
            tab.append(next(iterator))
        except StopIteration:
            break
    return tab


def main():
    print(select(gen_kwadrat(), 10))
    li = [2, 3, 1, 2]
    print(select(li, 10))

    trojki = ((a, b, c)for c in gen_calkowite() for b in range(1, c) for a in range(1, b) if a ** 2 + b ** 2 == c ** 2)
    print(select(trojki, 15))


if __name__ == '__main__':
    main()
