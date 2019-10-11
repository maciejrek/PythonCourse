class Author:
    """
    Author of the book, with the following properties:

    Attributes:
        name: A string representing author's name
        surname: A string representing author's surname
    """

    def __init__(self, uid: int, name: str, surname: str, is_active: bool):
        self.uid = uid
        self.aut_name = name
        self.aut_surname = surname
        self.aut_is_active = is_active

    @property
    def fullname(self):
        return self.aut_name + " " + self.aut_surname

    def __repr__(self):
        return f"[Author: {self.fullname}]"
