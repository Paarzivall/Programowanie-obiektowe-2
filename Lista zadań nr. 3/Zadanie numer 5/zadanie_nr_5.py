def generator_liczb_pierwszych():
    tab = [] # pomocnicza lista w której będą zapisywane liczby pierwsze
    i = 2 # liczba 2 jest 1 liczbą pierwszą
    while True:
        if tab.__len__() < 10000:
            for j in tab:  # przejście po liście z liczbami pierwszymi
                if i % j == 0:  # sprawdzenie czy i jest dzielnikiem tej liczby
                    break
            else:  # a jesli nie ma mniejszej od i liczby pierwszej z tab ktora jest jej dzielnikiem to i jest liczba pierwsza
                yield i
                tab.append(i)
            i += 1
        else:
            break


def main():
    file = open("liczby.txt", "w+")

    for i in generator_liczb_pierwszych():
        print(i)
        tmp = str(i) + "\n"
        file.write(tmp)
    file.close()


if __name__ == '__main__':
    main()