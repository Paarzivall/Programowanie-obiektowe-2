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


def menu():
    ile = int(input("Podaj do którego wyrazu chcesz wypisać ciąg Fibonacciego:\t"))
    fibonacci = Fibonacci()
    myiter = iter(fibonacci)
    for i in range(ile):
        print(f"{i + 1} wyraz ciągu:\t{int(next(myiter))}")


if __name__ == '__main__': menu()