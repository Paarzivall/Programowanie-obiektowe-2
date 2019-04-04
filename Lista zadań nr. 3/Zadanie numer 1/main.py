import authorization_system as auth
import all_errors as errors
import sys


class Editor(object):
    def __init__(self):
        self.username = None
        self.options = {
            "a": self.login,
            "b": self.test,
            "c": self.change,
            "d": self.quit
        }

    def login(self):
        login = input("Podaj login:\t")
        haslo = input("Podaj hasło:\t")

        try:
            auth.authenticator.login(login, haslo)
            self.username = login
        except errors.IncorrectUsername:
            print("Niepoprawna nazwa użykownika!")
        except errors.IncorrectPassword:
            print("Niepoprawne hasło!")

    def is_permitted(self, permission):
        try:
            return auth.authorizor.check_permission(self.username, permission)
        except errors.NotLoggedError:
            print("Użytkownik jest niezalogowany!!!")
            return False
        except errors.NotPermittedError:
            print("Zbyt małe uprawnienia!!!")
            return False
        except errors.PermissionError:
            print("Nieznane uprawnienia!!!")
            return False

    def test(self):
        if self.is_permitted("test"):
            print("Testowanie...")

    def change(self):
        if self.is_permitted("change"):
            print("Zmienianie...")

    def quit(self):
        sys.exit()

    def run(self):
        action = input(f"\t\t\t---MENU---\n[a]\tZaloguj się,\n[b]\tTestuj,\n[c]\tZmień,\n[d]\tZakończ.\n")
        if not action in self.options:
            print("Brak podanej opcji!!!\n")
        else:
            self.options[action]()


def menu():
    edit = Editor()
    while True:
        edit.run()

if __name__ == '__main__': menu()