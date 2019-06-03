from abc import ABC, abstractmethod


class Storage(object):
    _count = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls._count
        self.storage_name = f'_{prefix}#{index}'
        cls._count += 1

    def __get__(self, instance, owner):
        """
            jeżeli wywołanie nie nastąpi przez instancję zwraca deskryptor,
            w przeciwnym wypadku zwróci wartość atrybutu
        """
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        """
            sprawdza poprawność
        """
        setattr(instance, self.storage_name, value)


class Validated(ABC, Storage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abstractmethod
    def validate(self, instance, value):
        """
            zwraca zweryfikowaną wartość bądź wyjątek
        """


class ColorValidator(Validated):

    def validate(self, instance, value):
        colors = ['blue', 'green', 'black', 'red', 'pink']

        if len(value) > 0 and value.isalpha():
            for i in colors:
                if i == value:
                    return value
            else:
                raise ValueError("Brak takiego koloru")
        else:
            raise ValueError("Brak koloru")


class SideValidator(Validated):

    def validate(self, instance, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Błędna Wartość")
        else:
            if value > 0.0:
                return value
            else:
                raise ValueError("Błędna Wartość")


class AngleValidator(Validated):

    def validate(self, instance, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Błędna Wartość")
        else:
            if value <= 90.0:
                return value
            else:
                raise ValueError("Błędna Wartość")