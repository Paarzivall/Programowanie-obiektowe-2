class Smartphone(object):
    """
    __ <- 2 znaki podkreślenia w pythonie oznacza to że  atrybut jest prywarny
    """
    def __init__(self, manufacturer, model, price):
        """konstruktor parametrowy """
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    def return_manufacturer(self):
        return self.__manufacturer

    def return_model(self):
        return self.__model

    def return_price(self):
        return self.__price

    def __str__(self):
        return f"Producent: {self.return_manufacturer()},\nModel: {self.return_model()},\nCena: {self.return_price()}.\n"

# smartphone = Smartphone("LG", "G4", 234)
# print(f"{smartphone}")
