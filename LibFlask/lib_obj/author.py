class Author:
    """
    Author of the book, with the following properties:

    Attributes:
        name: A string representing author's name
        surname: A string representing author's surname
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
        return f"[Author: {self.fullname}]"


    def serialize(self):
        return {'uid': self.uid, 'name': self.name, 'surname': self.surname, 'active': self.active}