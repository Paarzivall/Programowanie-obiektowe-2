import zadanie_nr_2

coin = zadanie_nr_2.Coin()
for i in range(15):
    coin.throw()
    print(f"Rzut nr.: {i + 1}: {coin.show_side()}")