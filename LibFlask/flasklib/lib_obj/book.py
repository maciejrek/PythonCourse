from flasklib.lib_obj import author as aut
from flasklib.lib_obj import category as cat


class Book:
    """ This is a book class

    Attributes:
        author : A string representing book's author
        isbn : A string representing international standard book number
        category : A string representing book's category. It's defined in another module
        is_available : A bool containing information, if book's available in library
        """

    def __init__(self, uid: int, title: str, isbn: int, category: int, author: int, is_active: bool = True):
        self.uid = uid
        self.author = author
        self.title = title
        self.isbn = isbn
        self.category = category
        self.active = is_active

    def __repr__(self):
        return f"[Book {self.title} author id {self.author}, isbn: {self.isbn}, " \
               f"category id {self.category}, is active: {self.active}]"

    def serialize(self):
        return {'uid': self.uid, 'author': self.author, 'title': self.title, 'isbn': self.isbn,
                'category': self.category, 'active': self.active}


class BookObj:
    def __init__(self, uid: int, title: str, isbn: int, category: cat.Category, author: aut.Author,
                 is_active: bool = True):
        self.uid = uid
        self.author = author
        self.title = title
        self.isbn = isbn
        self.category = category
        self.active = is_active

        def __repr__(self):
            return f"[Book {self.title} author {self.author.fullname}, isbn: {self.isbn}, " \
                   f"category {self.category.name}, is active: {self.active}]"
