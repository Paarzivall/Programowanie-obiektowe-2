class RocketEngine(object):
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False):
        """Konstruktor parametrowy klasy RocketEngine"""
        self._name = name
        self._power = power
        self._working = working
        RocketEngine.count += 1

    def start(self):
        """Start silnika rakiety"""
        if self._working == False:
            RocketEngine.all_power += self._power
            self._working = True

    def stop(self):
        """Zatrzymanie silnika"""
        if self._working == True:
            RocketEngine.all_power -= self._power
            self._working = False

    def __str__(self):
        """Raportowanie o stanie silnika"""
        if self._working == True:
            work = "Tak"
        else:
            work = "Nie"
        return f"Silnik o nazwie: {self._name},\nMoc: {self._power}, Stan: {work}"

    def __del__(self):
        """Usunięcie 'dematerializacja' silnika"""
        RocketEngine.count -= 1

    @staticmethod
    def status():
        """Wypisanie raportu o aktualnie działających silnikach"""
        print(f"Silników pracujących: {RocketEngine.count},\nŁączna moc silników pracujących: {RocketEngine.all_power}")


def symulacja():
    print("\t\tStatek jest w porcie")

    engine_1 = RocketEngine("Silnik manewrowy 1", 50)
    engine_2 = RocketEngine("Silnik manewrowy 2", 50)

    print("\n\t\tPrzeprowadzanie manewrów:")
    engine_1.start()
    engine_2.start()
    RocketEngine.status()

    print("\n\t\tRozpędzenie statku w celu przejścia w hiperprędkość")
    engine_1.stop()
    engine_2.stop()
    engine_3 = RocketEngine("Silnik rozpędzający 1", 500)
    engine_4 = RocketEngine("Silnik rozpędzający 2", 500)
    engine_3.start()
    engine_4.start()
    RocketEngine.status()

    print("\n\t\tLot w hiperprędkości")
    engine_3.stop()
    engine_4.stop()
    engine_5 = RocketEngine("Silnik hiperprędkości 1", 400000)
    engine_6 = RocketEngine("Silnik hiperprędkości 2", 400000)
    engine_5.start()
    engine_6.start()
    RocketEngine.status()

    print("\n\t\tZmniejszenie prędkości")
    engine_5.stop()
    engine_6.stop()
    del engine_5
    del engine_6
    engine_3.start()
    engine_4.start()
    RocketEngine.status()

    print("\n\t\tManewrowanie")
    engine_3.stop()
    engine_4.stop()
    del engine_3
    del engine_4
    engine_1.start()
    engine_2.start()
    RocketEngine.status()

    print("\n\t\tCumowanie w porcie")
    engine_1.stop()
    engine_2.stop()
    """Czy silniki do manewrowania powinny być usuwane?"""
    del engine_1
    del engine_2
    RocketEngine.status()

symulacja()