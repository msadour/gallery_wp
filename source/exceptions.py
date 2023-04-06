class UsernameNotExistException(Exception):
    def __init__(self):
        self.message = "This username doesn't exist"
        self.code = 400
        super().__init__(self.message)


class UsernameAlreadyExistException(Exception):
    def __init__(self):
        self.message = "This username is not available"
        self.code = 400
        super().__init__(self.message)


class WrongPasswordException(Exception):
    def __init__(self):
        self.message = "The password is wrong"
        self.code = 400
        super().__init__(self.message)


class WrongTokenException(Exception):
    def __init__(self):
        self.message = "Wrong token"
        self.code = 400
        super().__init__(self.message)


class NotTokenException(Exception):
    def __init__(self):
        self.message = "Token is mandatory"
        self.code = 400
        super().__init__(self.message)


class WrongFormatImageException(Exception):
    def __init__(self):
        self.message = "Wrong image format. Image must be jpg, jpeg, png or webp"
        self.code = 400
        super().__init__(self.message)
