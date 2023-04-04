class UsernameException(Exception):
    def __init__(self):
        self.message = "This username doesn't exist"
        super().__init__(self.message)


class WrongPassword(Exception):
    def __init__(self):
        self.message = "The password is wrong"
        super().__init__(self.message)
