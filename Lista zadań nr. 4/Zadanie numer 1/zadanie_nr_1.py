class Pupil(object):
    ratings = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        while True:
            if isinstance(value, str) and str.isalpha(value) and len(value) >= 3:
                self.__name = value
                break
            else:
                value = input("Podałeś niepoprawne imię, podaj nowe: ")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        while True:
            if isinstance(value, str) and str.isalpha(value) and len(value) >= 3:
                self.__surname = value
                break
            else:
                value = input("Podałeś niepoprawne nazwisko, podaj nowe: ")

    def complete_marks(self, subject, rating):
        while True:
            if rating in self.ratings:
                self.marks[subject] = rating
                break
            else:
                rating = input(f"Podaj ocene (dostępne oceny: {self.ratings}):\t")

    def print_marks(self):
        for i in self.marks:
            print(f"{i}: \t{self.marks[i]}")

    def mean(self):
        sum = 0
        count = 0
        for i in self.marks:
            count +=1
            sum += self.marks[i]
        return sum / count

    def __str__(self):
        return f"Imie: {self.__name}, Nazwisko: {self.__surname}, Średnia ocen:\t{self.mean()}"


class Student(Pupil):
    weights_range = (0, 1)

    def __init__(self, name, surname):
        Pupil.__init__(self, name, surname)
        self.weights = {}

    def complete_weights(self, subject, rating, weight):
        super().complete_marks(subject, rating)
        while True:
            if weight > self.weights_range[0] and weight <= self.weights_range[1]:
                self.weights[subject] = weight
                break
            else:
                weight = input(f"Podaj wagę(wagi w zakresie: {self.weights_range}):\t")

    def mean(self):
        sum_weights = 0
        sum_up = 0
        for i in self.marks.keys():
            sum_weights += self.weights[i]
            sum_up += (self.weights[i] * self.marks[i])
        return sum_up / sum_weights

    def __str__(self):
        return f"Imie: {super().name}, Nazwisko: {super().surname}, Średnia ocen:\t{self.mean()}"


if __name__ == '__main__':
    """name = input("Podaj imie:\t")
    surname = input("Podaj nazwisko:\t")
    pupil = Pupil(name, surname)
    while True:
        subject = input("Podaj przedmiot:\t")
        rating = float(input(f"Podaj ocene (dostępne oceny: {pupil.ratings}):\t"))
        pupil.complete_marks(subject, rating)
        action = int(input("Chcesz wprowadzić kolejny przedmiot (jeżeli tak wpisz '1'):\t"))
        if action != 1:
            break
    pupil.print_marks()
    print(pupil)"""

    name = input("Podaj imie:\t")
    surname = input("Podaj nazwisko:\t")
    student = Student(name, surname)
    while True:
        subject = input("Podaj przedmiot:\t")
        rating = float(input(f"Podaj ocene (dostępne oceny: {student.ratings}):\t"))
        weight = float(input(f"Podaj wagę(wagi w zakresie: {student.weights_range}):\t"))
        student.complete_weights(subject, rating, weight)
        action = int(input("Chcesz wprowadzić kolejny przedmiot (jeżeli tak wpisz '1'):\t"))
        if action != 1:
            break
    student.print_marks()
    print(student)

