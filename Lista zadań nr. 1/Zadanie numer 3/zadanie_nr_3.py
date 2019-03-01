class Account(object):
    def __init__(self, value):
        """Konstruktor parametrowy - tworzy nowe 'konto'"""
        self._balance = value

    def pay(self, money):
        """Powiększenie salda na koncie"""
        self._balance += money

    def take(self, money):
        """Wypłata z konta"""
        if self._balance - money < 0:
            print("Niewystarczające środki na koncie do wykonania operacji!")
        else:
            self._balance -= money

    def show_balance(self):
        """Zwraca ilość środków na koncie"""
        return self._balance

    def __str__(self):
        """wypisanie obiektu na ekran (funkcja print() niejawnie korzysta z tego)
            używamy gdy chcemy uzyskać 'ładny' wygląd wyświetlanej zmiennej"""
        return f"Środki na koncie: {round(self.show_balance(),2)}"

def test():
    start = 200

    print("\tZałożenie konta z saldem 200 złotych")
    acc = Account(start)
    print(f"\t\t{acc}")

    print("\tWpłata 10 złotych")
    acc.pay(10)
    print(f"\t\t{acc}")

    print("\tWypłata 200 złotych")
    acc.take(210)
    print(f"\t\t{acc}")

    print("\tWypłata 200 złotych")
    acc.take(10)
    print(f"\t\t{acc}")

test()