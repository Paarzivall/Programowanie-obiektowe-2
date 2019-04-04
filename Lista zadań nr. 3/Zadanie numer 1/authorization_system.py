import hashlib
import all_errors as errors

class User(object):
    def __init__(self, username, password):
        self._username = username
        self._password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        hasher = hashlib.sha256()
        hasher.update(bytes(password, encoding="utf-8"))
        return hasher.digest()

    def check_password(self, password):
        if self._password == self._encrypt_password(password):
            return True
        else:
            return False


class Authenticator(object):
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise errors.UsernameAlreadyExists()
        elif len(password) <= 7:
            raise errors.PasswordTooShort()
        else:
            self.users[username] = User(username, password)

    def login(self, username, password):
        if not username in self.users:
            raise errors.IncorrectUsername()
        elif not self.users[username].check_password(password):
            raise errors.IncorrectPassword()
        else:
            self.users[username].is_logged = True
            return True

    def is_logged_in(self, username):
        if not username in self.users:
            raise  errors.IncorrectUsername()
        else:
            return self.users[username].is_logged


class Authorizor(object):
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        if permission in self.permissions:
            raise PermissionError()
        else:
            self.permissions[permission] = []

    def permit_user(self, username, permission):
        if not username in self.authenticator.users:
            raise errors.IncorrectUsername()
        elif not permission in self.permissions:
            raise PermissionError()
        else:
            self.permissions[permission].append(username)

    def check_permission(self, username, permission):
        if not self.authenticator.is_logged_in(username):
            raise errors.NotLoggedError()
        elif not permission in self.permissions:
            raise PermissionError()
        elif not username in self.permissions[permission]:
            raise errors.NotPermittedError()
        else:
            return True


authenticator = Authenticator()
authorizor = Authorizor(authenticator)
authenticator.add_user("user1", "qwertyu123")
authenticator.add_user("user2", "zxcv1234")
authorizor.add_permission("test")
authorizor.add_permission("change")
authorizor.permit_user("user1", "test")
authorizor.permit_user("user2", "change")