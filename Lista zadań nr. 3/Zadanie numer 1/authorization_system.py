import hashlib


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        return hashlib.sha256(password)

    def check_password(self, password):
        if self.password == hashlib.sha256(password):
            return True
        else:
            return False

    def __str__(self):
        return f"Login: {self.username},\tHasło: {self.password}"


class AuthenticException(Exception):
    def __init__(self, username, password):
        self.username = username
        self.password = password


def menu():
    user = User("ja", b"asdf")
    print(user)

    print(f"{user.check_password(b'asdf')}")


if __name__ == '__main__':
    menu()
