class User:
    """
    User of the book, with the following properties:

    Attributes:
        name: A string representing user's name
        surname: A string representing user's surname
    """

    def __init__(self, uid: int, name: str, surname: str, is_active: bool):
        self.uid = uid
        self.name = name
        self.surname = surname
        self.active = is_active

    @property
    def fullname(self):
        return self.name + " " + self.surname

    def __repr__(self):
        return f"[User: {self.fullname}]"
