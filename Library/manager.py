import users_database as ub
import book_database as bb
import author_database as ab
import book_category_database as bcb
import json


class LibraryManager:
    """
    Manager of the library. Stores every needed data ( like list of book categories ).
    Manager has the following properties:

    Attributes:
    """

    def __init__(self):
        self.book_category_database = bcb.BookCategoryDataBase('book_category_db.json')
        self.user_database = ub.UserDataBase('users_db.json')
        self.author_database = ab.AuthorDataBase('author_db.json')
        self.book_database = bb.BookDataBase('book_db.json')
        self.history = self.load_history('history.json')

    def loan_a_book(self, book_isbn: str, user_id: str):
        if not self.user_database.is_user_in_db(user_id) or not self.book_database.is_book_in_db(book_isbn):
            return False
        if self.book_database.loan_book(book_isbn, user_id):
            # logger success
            self.history['Book'][book_isbn].append(user_id)
            self.history['User'][user_id].append(book_isbn)
            self.book_database.save_books()
            self.save_history('history.json')
            return True
        # logger error
        return False

    def return_a_book(self, book_isbn: str):
        if self.book_database.return_a_book(book_isbn):
            # logger success
            self.book_database.save_books()
            self.save_history('history.json')
            return True
        # logger error
        return False

    def list_by_category(self):
        cat_list = self.book_category_database.return_list()
        cat_dict = self.book_database.return_dict_by_category()
        return cat_dict

    def load_history(self, file_dir: str):
        temp_dict = {'Book': dict(), 'User': dict()}
        try:
            with open(file_dir, 'r') as file:
                x = json.load(file)
                temp_dict['Book'] = x['Book']
                temp_dict['User'] = x['User']
                return temp_dict
        except FileNotFoundError:
            temp_dict = {'Book': dict(), 'User': dict()}
            for i in self.book_database.book_dict:
                temp_dict['Book'][i] = list()
            for i in self.user_database.user_dict:
                temp_dict['User'][i] = list()
            return temp_dict

    def save_history(self, file_dir: str):
        with open(file_dir, 'w') as file:
            json.dump(self.history, file, indent=2)
