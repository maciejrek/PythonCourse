class MyBook:
    """ This is a book class

    Attributes:
        author : A string representing book's author
        isbn : A string representing international standard book number
        category : A string representing book's category. It's defined in another module
        is_available : A bool containing information, if book's available in library
        """

    def __init__(self, author: str, title: str, isbn: str, category: str, owner: str = '0', avail: bool = True):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.owner = owner
        self.category = category
        self.is_available = avail

    def __repr__(self):
        return f"[Book {self.title} author id {self.author}, isbn: {self.isbn}, owner id {self.owner}, " \
               f"category id {self.category}, is available: {self.is_available}]"

    def prepare_to_json(self):
        return {'title': self.title, 'author': self.author, 'isbn': self.isbn, 'owner': self.owner,
                'category': self.category, 'availability': self.is_available}

