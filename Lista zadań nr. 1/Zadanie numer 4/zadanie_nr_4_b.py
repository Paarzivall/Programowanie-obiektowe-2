import pickle
import zadanie_nr_4

ile = int(input(f"Podaj ile obiektów chcesz wprowadzić i zapisać do pliku: "))

file = open('phones.dat', 'wb+')
for i in range(ile):
    manufacturer = input(f"\nPodaj producenta telefonu: ")
    model = input(f"Podaj model telefonu: ")
    price = input(f"Podaj cenę telefonu: ")
    smartphone = zadanie_nr_4.Smartphone(manufacturer, model, price)
    pickle.dump(smartphone, file)

file.close()

action = int(input(f"[1] Odczytaj z pliku,\n[2] Zakończ"))
if action == 1:
    file = open('phones.dat', 'rb')
    zawartosc = []

    for i in range(ile):
        """Wczytanie do listy zawartośći pliku"""
        zawartosc.append(pickle.load(file))

    for j in zawartosc:
        """Wypisanie na ekran listy z zawartością pliku"""
        print(f"{j}")