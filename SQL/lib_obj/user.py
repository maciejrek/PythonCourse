class User:
    """
    User of the book, with the following properties:

    Attributes:
        name: A string representing user's name
        surname: A string representing user's surname
    """

    def __init__(self, uid: int, name: str, surname: str, is_active: bool):
        self.usr_id = uid
        self.usr_name = name
        self.usr_surname = surname
        self.usr_is_active = is_active

    @property
    def fullname(self):
        return self.usr_name + " " + self.usr_surname

    def __repr__(self):
        return f"[User: {self.fullname}]"
