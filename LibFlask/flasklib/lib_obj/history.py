from datetime import datetime
from flasklib.lib_obj import book, user


class History:
    """
    History of the book, with the following properties:

    Attributes:
    """

    def __init__(self, uid: int, id_book: int, id_user: int, date_in: datetime, date_out: datetime):
        self.uid = uid
        self.book_id = id_book
        self.user_id = id_user
        self.date_in = date_in
        self.date_out = date_out


class HistoryObj:
    """
    History of the book, with the following properties:

    Attributes:
    """

    def __init__(self, uid: int, bk: book.Book, usr: user.User, date_in: datetime, date_out: datetime):
        self.uid = uid
        self.book = bk
        self.user = usr
        self.date_in = date_in
        self.date_out = date_out
