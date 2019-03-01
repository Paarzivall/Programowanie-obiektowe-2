import random


class Coin(object):
    def __init__(self):
        """Konstruktor bezparametrowy"""
        if random.randrange(2) == 0:
            self.side = "orzeł"
        else:
            self.side = "reszka"

    def throw(self):
        """Wylosowanie strony monety"""
        if random.randrange(2) == 0:
            self.side = "orzeł"
        else:
            self.side = "reszka"

    def show_side(self):
        """Wyświetlenie na ekran obiektu"""
        return self.side


def test():
    """Funkcja sterująca - służy do testów"""
    coin1 = Coin()
    coin2 = Coin()
    coin3 = Coin()
    coin1.throw()
    coin2.throw()
    coin3.throw()
    print(f"Rzut 1: {coin1.show_side()}")
    print(f"Rzut 2: {coin2.show_side()}")
    print(f"Rzut 3: {coin3.show_side()}")

# test()