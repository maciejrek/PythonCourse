from lib_db import LibDb
from lib_obj.history import History, HistoryObj
from lib_obj.book import Book
from lib_obj.user import User
from datetime import datetime


def get_history_dict(db: LibDb.LibDb):
    hist_db = db.return_tab("history")
    hist_dict = dict()
    for i in hist_db:
        uid, book_id, user_id, date_in, date_out = i
        hist_dict[uid] = History(uid, book_id, user_id, date_in, date_out)
    return hist_dict


def get_history_dict_by_user(db: LibDb.LibDb):
    hist_dict = get_history_dict(db)
    by_user = dict()
    for i in hist_dict:
        if hist_dict[i] not in by_user:
            by_user[hist_dict[i].user_id] = list()
        by_user[hist_dict[i].user_id].append(hist_dict[i].book_id)
    return by_user


def get_history_dict_by_book(db: LibDb.LibDb):
    hist_dict = get_history_dict(db)
    by_book = dict()
    for i in hist_dict:
        if hist_dict[i] not in by_book:
            by_book[hist_dict[i].book_id] = list()
        by_book[hist_dict[i].book_id].append(hist_dict[i].user_id)
    return by_book


def get_history_obj_list(db: LibDb.LibDb):
    hist_db = db.return_tab("history")
    hist_list = list()
    for i in hist_db:
        uid, book_id, user_id, date_in, date_out = i
        hist_list.append(History(uid, book_id, user_id, date_in, date_out))
    return hist_list


def get_history_list_by_user(db: LibDb.LibDb, user_id: int):
    hist_dict = get_history_dict_by_user(db)
    if user_id not in hist_dict.keys():
        return []
    temp_list = hist_dict[user_id]
    return [i for i in temp_list]


def get_history_list_by_book(db: LibDb.LibDb, book_id: int):
    hist_dict = get_history_dict_by_book(db)
    if book_id not in hist_dict.keys():
        return []
    temp_list = hist_dict[book_id]
    return [i for i in temp_list]


def get_book_status(db: LibDb.LibDb, book_id: int):
    temp = db.return_tab_by_category("history", "id_book", book_id)
    if not temp:
        return True
    _, _, _, time_borrow, time_return = temp[-1]
    return time_borrow < time_return


def borrow_a_book(db: LibDb.LibDb, book_id: int, usr_id: int):
    return db.borrow_a_book(book_id, usr_id)


def return_a_book(db: LibDb.LibDb, book_id: int):
    return db.return_a_book(book_id)


def create_history_obj(uid: int, bk: Book, usr: User, date_in: datetime, date_out: datetime):
    return HistoryObj(uid, bk, usr, date_in, date_out)
