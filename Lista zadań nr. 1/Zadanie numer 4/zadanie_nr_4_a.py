import zadanie_nr_4

ile = int(input("Podaj ilość elementów listy:"))

obiekty = []

for i in range(ile):
    manufacturer = input(f"\nPodaj producenta telefonu: ")
    model = input(f"Podaj model telefonu: ")
    price = input(f"Podaj cenę telefonu: ")
    obiekty.append(zadanie_nr_4.Smartphone(manufacturer, model, price))
    # print(obiekty[i])


action = input("[1] Wyświetl listę,\n[2] Zakończ\n")
action = int(action)
if action == 1:
    for i in range(ile):
        print(obiekty[i])