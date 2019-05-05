from abc import ABC, abstractmethod
from numbers import Real

class Temperature(ABC):
    @abstractmethod
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"\n{round(self.temperature)} stopni w skali: {self.__class__.__name__}"

    def __repr__(self):
        return self.__class__.__name__ + f" ({self.temperature})"

    def above_freezing(self):
        if self.convert_to_Celcius().temperature > 0:
            return True
        else:
            return False

    @abstractmethod
    def convert_to_Celcius(self):
        pass

    def convert_to_Kelvin(self):
        pass

    def convert_to_Farenheit(self):
        pass

    @property
    @abstractmethod
    def temperature(self):
        return self._temperature

    @temperature.setter
    @abstractmethod
    def temperature(self, temperature):
        if isinstance(temperature, Real):
            self._temperature = temperature
        else:
            self._temperature = 0


class Farenheit(Temperature):

    def __init__(self, temperature):
        super().__init__(temperature)

    def convert_to_Farenheit(self):
        return self

    def convert_to_Celcius(self):
        return Celsius((self.temperature - 32)*0.556)

    def convert_to_Kelvin(self):
        return Kelvin((self.convert_to_Celcius().temperature) + 273.16)

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, temperature):
        super(type(self), type(self)).temperature.__set__(self, temperature)


class Celsius(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def convert_to_Farenheit(self):
        return Farenheit(32 + 1.8 * self.temperature)

    def convert_to_Celcius(self):
        return self

    def convert_to_Kelvin(self):
        return Kelvin(self.temperature + 273.16)

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, temperature):
        super(type(self), type(self)).temperature.__set__(self, temperature)


class Kelvin(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def convert_to_Farenheit(self):
        return Farenheit((self.convert_to_Celcius().temperature / 0.556) + 32)

    def convert_to_Celcius(self):
        return Celsius(self.temperature - 273.16)

    def convert_to_Kelvin(self):
        return self

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, temperature):
        super(type(self), type(self)).temperature.__set__(self, temperature)


obj = Farenheit(50)
print(obj)
print(repr(obj))

list = [Celsius(-20), Celsius(500), Celsius(10),
        Farenheit(10), Farenheit(100), Farenheit(50), Farenheit(44),
        Kelvin(-100), Kelvin(-50), Kelvin(10), Kelvin(100)]

list_farenheit = []
list_celsius = []
list_kelvin = []

for i in list:
    print(i, "\n", repr(i))
    if i.above_freezing():
        print("Powyżej zera")

    list_farenheit.append(i.convert_to_Farenheit())
    list_celsius.append(i.convert_to_Celcius())
    list_kelvin.append(i.convert_to_Kelvin())
    print(50* "-")

for i in list_farenheit:
    if not i.above_freezing():
        print(i)
    print("\nLista Farenheit poniżej zamarzania\n")
    print(50*"-")
print(100*"*")

for i in list_celsius:
    if not i.above_freezing():
        print(i)
    print("\nLista Celsius poniżej zamarzania\n")
    print(50*"-")
print(100*"*")

for i in list_kelvin:
    if not i.above_freezing():
        print(i)
    print("\nLista Kelvin poniżej zamarzania\n")
    print(50*"-")
print(100*"*")