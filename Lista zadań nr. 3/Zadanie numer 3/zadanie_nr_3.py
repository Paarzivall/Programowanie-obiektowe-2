import itertools


class Fibonacci(object):

    def __init__(self):
        self.licznik = 0

    def __iter__(self):
        self.licznik = 0
        return self

    def __next__(self):
        n = self.licznik
        self.licznik += 1
        xz = 0
        xf = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(n):
                tmp = xz + xf
                xz = xf
                xf = tmp
            return xz


def fibonacci_generator():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second


class Fibonacci_iter(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        licznik = 0
        iteruj = iter(fibonacci_generator())
        while licznik < self.start:
            next(iteruj)
            licznik += 1
        while licznik < self.stop:
            yield next(iteruj)
            licznik += 1
        return


def menu():
    ile = int(input("Podaj do którego wyrazu chcesz wypisać ciąg Fibonacciego:\t"))
    fibonacci = Fibonacci()
    myiter = iter(fibonacci)
    for i in range(ile):
        print(f"{i + 1} wyraz ciągu:\t{int(next(myiter))}")

    print(next(itertools.islice(fibonacci_generator(), 100000, 100001)))

    with open('liczby.txt', 'w') as f:
        first = True
        for i in Fibonacci_iter(100000, 100020):
            f.write(f'{i}\n')
            if first:
                print(f'Ilosc cyfr F(100000): {len(str(i))}')
                first = False


if __name__ == '__main__': menu()