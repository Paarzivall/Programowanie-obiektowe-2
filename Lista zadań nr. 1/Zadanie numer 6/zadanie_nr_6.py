class TV:
    kanal_min = 1
    kanal_max = 30
    glos_min = 0
    glos_max = 70

    def __init__(self, kanal, glos):
        self._kanal = kanal
        self._glos = glos

    def __str__(self):
        return f"Włączono kanał: {self._kanal}, Głośność: {self._glos}"

    def zmien_kanal(self, kanal):
        if TV.kanal_min <= kanal <= TV.kanal_max and kanal != self._kanal:
            self._kanal = kanal
            print(f"Kanał zmieniony. Obecny kanał to: {self._kanal}, Głośność: {self._glos}")
        else:
            action = 1
            while action == 1:
                kanal = int(input("Podaj kanał: "))
                if TV.kanal_min <= kanal <= TV.kanal_max and kanal != self._kanal:
                    self._kanal = kanal
                    print(f"Kanał zmieniony. Obecny kanał to: {self._kanal}, Głośność: {self._glos}")
                    action = 0
                else:
                    print(f"Kanał o numerze: {kanal} nie istnieje. Podaj inny numer kanału!")


    def zmien_glos(self, glos):
        if TV.glos_min <= glos <= TV.glos_max and glos != self._glos:
            self._glos = glos
            print(f"Głośność zmieniona. Obecny kanał to: {self._kanal}, Głośność: {self._glos}")
        else:
            action = 1
            while action == 1:
                glos = int(input("Podaj głośność: "))
                if TV.glos_min <= glos <= TV.glos_max and glos != self._glos:
                    self._glos = glos
                    print(f"Głośność zmieniona. Obecny kanał to: {self._kanal}, Głośność: {self._glos}")
                    action = 0
                else:
                    print(f"Zbyt duża głośność")

    def return_kanal(self):
        return self._kanal

    def return_glos(self):
        return  self._glos

    def __del__(self):
        print("Telewizor został wyłączony")


def TV_on():
    action = 1

    while action == 1:
        kanal = int(input("Podaj numer kanału który chcesz włączyć: "))
        if TV.kanal_min <= kanal <= TV.kanal_max:
            tv = TV(kanal, 12)
            action = 0
            work(tv)
        else:
            print(f"Kanał o numerze: {kanal} nie istnieje. Podaj inny numer kanału!")


def work(tv):
    print(tv)
    action = 1
    while action == 1:
        x = int(input("Co chcesz zrobić?:\n[1] Zmień kanał,\n[2] Zmień głośność,\n[3] Wyłącz telewizor."))

        if x == 1:
            newK = int(input(f"Podaj nowy kanał. Obecny kanał to {tv.return_kanal()}:"))
            tv.zmien_kanal(newK)
        elif x == 2:
            newS = int(input(f"Podaj nową głośność. Obecna głośność to {tv.return_glos()}:"))
            tv.zmien_glos(newS)
        else:
            del tv
            action = 0


TV_on()