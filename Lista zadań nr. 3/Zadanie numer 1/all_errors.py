class AuthenticException(Exception):
    def __init__(self, username = None, user = None):
        self._username = username
        self._user = user


class PermissionError(Exception):
    pass


class IncorrectPassword(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    pass


class NotPermittedError(AuthenticException):
    pass