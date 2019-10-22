from flasklib.lib_obj.book import Book
from flasklib.lib_obj.book import BookObj
from flasklib.lib_obj import author
from flasklib.lib_obj import category
from flasklib.lib_db import LibDb


def get_book_dict(db: LibDb.LibDb):
    book_db = db.return_tab("book")
    book_dict = dict()
    for i in book_db:
        uid, title, aut_id, cat_id, isbn, active = i
        book_dict[uid] = Book(uid, title, isbn, cat_id, aut_id, active)
    return book_dict


def create_book_obj(uid: int, title: str, isbn: int, cat: category.Category, aut: author.Author):
    return BookObj(uid, title, isbn, cat, aut)


def deactivate_book(db: LibDb.LibDb, uid: int):
    db.set_inactive("book", uid)


def activate_book(db: LibDb.LibDb, uid: int):
    db.set_active("book", uid)


def get_book_by_id(db: LibDb.LibDb, uid: int):
    book_dict = get_book_dict(db)
    return book_dict[uid]
