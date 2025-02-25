from lib_db import *


class LibraryManager:

    def __init__(self):
        self.database = LibDb.prepare_database("LibraryDatabase")

    @staticmethod
    def get_users_dict(db: LibDb.LibDb):
        return user_db.get_user_dict(db)

    @staticmethod
    def get_user_list(db: LibDb.LibDb):
        return user_db.get_user_list(db)

    @staticmethod
    def get_category_dict(db: LibDb.LibDb):
        return category_db.get_category_dict(db)

    @staticmethod
    def get_category_list(db: LibDb.LibDb):
        return category_db.get_category_list(db)

    @staticmethod
    def get_book_dict(db: LibDb.LibDb):
        return book_db.get_book_dict(db)

    @staticmethod
    def get_book_dict_by_cat(db: LibDb.LibDb):
        return book_db.get_book_dict_by_cat(db)

    @staticmethod
    def get_book_list(db: LibDb.LibDb):
        return book_db.get_book_list(db)

    @staticmethod
    def get_authors_dict(db: LibDb.LibDb):
        return author_db.get_author_dict(db)

    @staticmethod
    def get_author_list(db: LibDb.LibDb):
        return author_db.get_author_list(db)

    @staticmethod
    def get_history_dict(db: LibDb.LibDb):
        return history_db.get_history_dict(db)

    @staticmethod
    def get_history_dict_by_user(db: LibDb.LibDb):
        return history_db.get_history_dict_by_user(db)

    @staticmethod
    def get_history_list_by_user(db: LibDb.LibDb, user_id: int):
        return history_db.get_history_list_by_user(db, user_id)

    @staticmethod
    def get_history_list_by_book(db: LibDb.LibDb, book_id: int):
        return history_db.get_history_list_by_book(db, book_id)

    @staticmethod
    def get_history_dict_by_book(db: LibDb.LibDb):
        return history_db.get_history_dict_by_book(db)

    @staticmethod
    def create_book(uid: int, title: str, isbn: int, category: int, author: int):
        return book_db.create_book(uid, title, isbn, category, author)

    @staticmethod
    def is_book_in_library(db: LibDb.LibDb, book_id: int):
        return history_db.get_book_status(db, book_id)

    @staticmethod
    def borrow_a_book(db: LibDb.LibDb, book_id: int, usr_id: int):
        return history_db.borrow_a_book(db, book_id, usr_id)

    @staticmethod
    def return_a_book(db: LibDb.LibDb, book_id: int):
        return history_db.return_a_book(db, book_id)

    @staticmethod
    def deactivate_book(db: LibDb.LibDb, book_id: int):
        return book_db.deactivate_book(db, book_id)

    @staticmethod
    def activate_book(db: LibDb.LibDb, book_id: int):
        return book_db.activate_book(db, book_id)

    @staticmethod
    def deactivate_user(db: LibDb.LibDb, user_id: int):
        return user_db.deactivate_user(db, user_id)

    @staticmethod
    def activate_user(db: LibDb.LibDb, user_id: int):
        return user_db.activate_user(db, user_id)

    @staticmethod
    def deactivate_category(db: LibDb.LibDb, category_id: int):
        return category_db.deactivate_category(db, category_id)

    @staticmethod
    def activate_category(db: LibDb.LibDb, category_id: int):
        return category_db.activate_category(db, category_id)

    @staticmethod
    def deactivate_author(db: LibDb.LibDb, author_id: int):
        return author_db.deactivate_author(db, author_id)

    @staticmethod
    def activate_author(db: LibDb.LibDb, author_id: int):
        return author_db.activate_author(db, author_id)
