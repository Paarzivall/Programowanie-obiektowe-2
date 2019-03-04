class Pet(object):

    def __init__(self, name, hunger=0, tiredness=0):
        """Konstruktor parametrowy klasy Pet"""
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness

    def __passage_of_time(self):
        """metoda w której zwiększamy poziom głodu i znucdzenia zwierzaka podczas wykonywania jakiś czynności"""
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        """metoda reprezentująca nastrój zwierzaka"""
        poziom = self.hunger + self.tiredness
        print(f"\t\t\tPoziom: {poziom}")
        if poziom < 5:
            return 'szczęśliwy'
        elif 5 <= poziom < 10:
            return 'zadowolony'
        elif 10 <= poziom < 15:
            return 'podenerwowany'
        elif poziom >= 15:
            return 'wściekły'

    def talk(self):
        """Informuje o nastroju zwierzaka"""
        self.__passage_of_time()
        print(f"\t\tZwierzak jest {self.mood}")

    def eat(self, food=4):
        """Metoda w której dzięki której karmimy zwierzaka"""
        if (self.hunger - food) < 0:
            self.hunger = 0
        else:
            self.hunger -= food
        print("\t\tZwierzak został nakarmiony. Zmniejszyłeś(-aś) mu poziom głodu, za to poziom znudzenia rośnie")
        self.__passage_of_time()

    def play(self, fun=4):
        """Metoda w której bawimy się ze zwierzakiem"""
        if (self.tiredness - fun) < 0:
            self.tiredness = 0
        else:
            self.tiredness -= fun
        print("\t\tPobawiłeś się ze swoim zwierzakiem. Zmniejszyłeś(-aś) mu poziom znudzenia, za to poziom głodu rośnie.")
        self.__passage_of_time()

    def __str__(self):
        return f"{self.name} ma głód na poziomie: {self.hunger} i znudzenie na poziomie: {self.tiredness}. Zwierzak jest {self.mood}"

    def __del__(self):
        print("\t\tZwierzak został uśpiony/zabity")


if __name__ == '__main__':
    name = input("Podaj imie zwierzaka: ")
    pet = Pet(name)
    print(f"\t\tStworzyłeś zwierzaka o imieniu {pet.name}")

    action = 1
    while action == 1:
        print("Co chcesz zrobić?")
        wybor = int(input(f"[1] Nakarm zwierza(głód: {pet.hunger})\n[2] Pobaw się ze zwierzem (znudzenie: {pet.tiredness})\n[3] Dowiedz się o nastroju zwierzaka \n[4] Dowiedz się o parametrach życiowych zwierzaka \n[5] Uśpij/Zabij zwierzaka"))

        if wybor == 1:
            pet.eat()
        elif wybor == 2:
            pet.play()
        elif wybor == 3:
            pet.talk()
        elif wybor == 4:
            print(pet)
        else:
            del pet
            action = 0


