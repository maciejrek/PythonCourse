class Author:
    """
    Author of the book, with the following properties:

    Attributes:
        name: A string representing author's name
        surname: A string representing author's surname
    """

    def __init__(self, uid: str, name: str, surname: str):
        self.uid = uid
        self.aut_name = name
        self.aut_surname = surname

    def __repr__(self):
        return f"[Author: {self.aut_name} {self.aut_surname}, (id {self.uid})]"

    def prepare_to_json(self):
        return {'name': self.aut_name, 'surname': self.aut_surname}