from lib_obj.book import Book
from lib_db import LibDb


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
        if book_dict[i].book_is_active:
            book_list.append(book_dict[i].title)
            book_id_list.append(i)
    return book_list, book_id_list


def create_book(uid: int, title: str, isbn: int, category: int, author: int):
    return Book(uid, title, isbn, category, author)


def deactivate_book(db: LibDb.LibDb, uid: int):
    db.set_inactive("book", uid)


def activate_book(db: LibDb.LibDb, uid: int):
    db.set_active("book", uid)
