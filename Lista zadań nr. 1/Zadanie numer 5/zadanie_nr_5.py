class RocketEngine(object):
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False):
        self.name = name
        self.power = power,
        self.working = working
        self.count += 1

    def start(self, power):
        if self.working == False:
            self.all_power = power
            self.working = True

    def stop(self):
        if self.working == True:
            self.all_power = self.power
            self.working = False

    def __str__(self):
        return f"\t\tAll Power: {self.all_power},\n\t\tCount: {self.count}"

    def __del__(self):
        self.count = self.count - 1

    @staticmethod
    def status(x, y):
        return f"{x},\n {y}"


def symulacja():
    print("\tAkcja:\tKosmiczny statek jest w porcie")
    moc_silnika = 0
    engine_1 = RocketEngine('Andromeda', moc_silnika)
    engine_2 = RocketEngine('Andromeda', moc_silnika)
    #print(f"{RocketEngine.status(engine_1, engine_2)}")
    print(f"{engine_1}")
    print(f"{engine_2}")

    print(f"\n\tAkcja:\tPrzeprowadzenie manewru")
    moc_silnika = 50
    engine_1.start(moc_silnika)
    engine_2.start(moc_silnika)
    print(f"{RocketEngine.status(engine_1, engine_2)}")

    print(f"\n\tAkcja:\tRozpędzenie się")
    moc_silnika = 500
    engine_1.stop()
    engine_2.stop()
    engine_3 = RocketEngine('Andromeda', moc_silnika)
    engine_4 = RocketEngine('Andromeda', moc_silnika)
    engine_3.start(moc_silnika)
    engine_4.start(moc_silnika)
    print(f"{RocketEngine.status(engine_3, engine_4)}")

    print(f"\n\tAkcja:\tPrzejście w hipernapęd")
    moc_silnika = 400000
    engine_3.stop()
    engine_4.stop()
    engine_5 = RocketEngine('Andromeda', moc_silnika)
    engine_6 = RocketEngine('Andromeda', moc_silnika)
    engine_5.start(moc_silnika)
    engine_6.start(moc_silnika)
    print(f"{RocketEngine.status(engine_5, engine_6)}")

    

symulacja()
