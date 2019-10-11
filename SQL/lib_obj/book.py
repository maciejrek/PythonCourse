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
        self.book_is_active = is_active

    def __repr__(self):
        return f"[Book {self.title} author id {self.author}, isbn: {self.isbn}, " \
               f"category id {self.category}, is active: {self.book_is_active}]"
