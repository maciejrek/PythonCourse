class User:
    """
    User of the book, with the following properties:

    Attributes:
        name: A string representing user's name
        surname: A string representing user's surname
    """

    def __init__(self, uid: str, name: str, surname: str):
        self.usr_id = uid
        self.usr_name = name
        self.usr_surname = surname

    def __repr__(self):
        return f"[User: {self.usr_name} {self.usr_surname}]"

    def prepare_to_json(self):
        return {'name': self.usr_name, 'surname': self.usr_surname}
