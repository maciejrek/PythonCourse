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


def get_book_dict_by_cat(db: LibDb.LibDb):
    book_dict = get_book_dict(db)
    by_cat = dict()
    for i in book_dict:
        if book_dict[i].category not in by_cat:
            by_cat[book_dict[i].category] = list()
        by_cat[book_dict[i].category].append(book_dict[i].title)
    return by_cat


def get_book_list(db: LibDb.LibDb):
    book_dict = get_book_dict(db)
    book_list = list()
    book_id_list = list()
    for i in book_dict:
        if book_dict[i].active:
            book_list.append(book_dict[i].title)
            book_id_list.append(i)
    return book_list, book_id_list


def get_book_obj_list(db: LibDb.LibDb):
    book_db = db.return_tab("book")
    book_list = list()
    for i in book_db:
        uid, title, aut_id, cat_id, isbn, active = i
        book_list.append(Book(uid, title, isbn, cat_id, aut_id, active))
    return book_list


def create_book(uid: int, title: str, isbn: int, cat: int, aut: int):
    return Book(uid, title, isbn, cat, aut)


def create_book_obj(uid: int, title: str, isbn: int, cat: category.Category, aut: author.Author):
    return BookObj(uid, title, isbn, cat, aut)


def deactivate_book(db: LibDb.LibDb, uid: int):
    db.set_inactive("book", uid)


def activate_book(db: LibDb.LibDb, uid: int):
    db.set_active("book", uid)


def get_book_by_id(db: LibDb.LibDb, uid: int):
    book_dict = get_book_dict(db)
    return book_dict[uid]
