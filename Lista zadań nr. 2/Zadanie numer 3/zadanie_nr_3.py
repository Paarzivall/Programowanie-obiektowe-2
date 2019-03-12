class Person(object):

    def __init__(self):
        self.name = input("Podaj imie:\t")
        self.surname = input("Podaj nazwisko:\t")
        self.age = int(input("Podaj wiek:\t"))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            self._name = "Nie podano"

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._surname = value
        else:
            self._surname = "Nie podano"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0 <= value <= 130:
            self._age = value
        else:
            self._age = 0

    def __str__(self):
        return f"Imie: {self._name}, Nazwisko: {self._surname}, Wiek: {self._age}"


class Student(Person):

    def __init__(self):
        Person.__init__(self)
        self.field_of_study = input("Podaj kierunek studiów:\t")
        self.student_book = {}
        self.add_student_book()

    def add_student_book(self):
        while True:
            subject = input("Podaj przedmiot:\t")
            grade = int(input("Podaj ocenę:\t"))
            while False:
                if grade < 1 or grade > 6:
                    grade = int(input("Podaj ocenę:\t"))
                else:
                    break
            self.student_book[subject] = grade
            x = int(input("Dodać kolejny prtzedmiot? (Wpisz '1' jeżeli chcesz kontynuować)"))
            if x != 1:
                break

    def __str__(self):
        all_info = super(Student, self).__str__()
        all_info += f"\nKierunek studiów: {self.field_of_study}"
        for grades in self.student_book:
            all_info += "\n"
            all_info += grades
            all_info += "\t"
            all_info += str(self.student_book[grades])
        return all_info


class Employee(Person):

    def __init__(self):
        Person.__init__(self)
        self.job_title = input("Podaj zawód:\t")
        self.skills = []
        self.add_skills()

    def add_skills(self):
        while True:
            skill = input("Podaj umiejętność:\t")
            self.skills.append(skill)
            x = int(input("Dodać kolejną umiejętność? (Wpisz '1' jeżeli chcesz kontynuować)"))
            if x != 1:
                break

    def __str__(self):
        all_info = super(Employee, self).__str__()
        all_info += f"\nZawód: {self.job_title}"
        for skill in self.skills:
            all_info += "\n"
            all_info += skill
        return all_info


def menu():
    student_list = []
    employee_list = []
    while True:
        action = int(input("[1] Dodaj studenta,\n[2] Wyświetl studentów\n[3] Dodaj pracownika\n[4] Wyświetl pracowników\n[5] Zakończ"))
        if action == 1:
            person = Student()
            student_list.append(person)
        elif action == 2:
            print("\n\n\t\t\tStudenci")
            for student in student_list:
                print(student)
        elif action == 3:
            person = Employee()
            employee_list.append(person)
        elif action == 4:
            print("\n\n\t\t\tPracownicy")
            for employee in employee_list:
                print(employee)
        else:
            break

if __name__ == '__main__':menu()
