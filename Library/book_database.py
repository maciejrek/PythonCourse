from typing import Iterable, Dict

import my_book
import json


class BookDataBase:
    """
    Users database, with the following properties:

    Attributes:
    """

    def __init__(self, file_name: str):
        self.save_directory = file_name
        self.load_directory = file_name
        self.book_dict: Dict[str, my_book.MyBook] = self.load_books()

    def load_books(self):
        try:
            with open(self.load_directory, 'r') as file:
                # logger : loading data from file
                x = json.load(file)
                temp_dict = dict()
                for i in x:
                    temp_dict[i] = my_book.MyBook(author=x[i]['author'], title=x[i]['title'], isbn=i,
                                                  category=x[i]['category'], owner=x[i]['owner'],
                                                  avail=x[i]['availability'])
                return temp_dict
        except FileNotFoundError:
            # logger : file does not exist
            return dict()

    def save_books(self):
        dic = dict()
        for i in self.book_dict:
            dic[i] = self.book_dict[i].prepare_to_json()
        with open(self.save_directory, 'w') as file:
            json.dump(dic, file, indent=2)

    # isbn as param cause i assume programmer know what he's doing
    def is_book_in_db(self, isbn: str):
        for i in self.book_dict:
            if i == isbn:
                return True
        return False

    # isbn as param cause i assume programmer know what he's doing
    def is_book_available(self, isbn: str):
        return self.book_dict[isbn].is_available

    def add_book(self, bk: my_book.MyBook):
        if not self.is_book_in_db(bk.isbn):
            self.book_dict[bk.isbn] = bk
            # logger : user added
            return True
        return False

    def remove_book(self, isbn: str):
        if self.is_book_in_db(isbn):
            del self.book_dict[isbn]
        return True

    def return_dict_by_author(self):
        temp = dict()
        id_list = list()
        for i in self.book_dict:
            temp[self.book_dict[i].author] = self.book_dict[i].title
            id_list.append(self.book_dict[i].isbn)
        return temp, id_list

    def return_dict_by_category(self):
        temp = dict()
        for i in self.book_dict:
            if self.book_dict[i].category not in temp:
                temp[self.book_dict[i].category] = list()
            temp[self.book_dict[i].category].append(self.book_dict[i].title)
        return temp

    def loan_book(self, book_isbn: str, user_id: str):
        if self.is_book_in_db(book_isbn) and self.is_book_available(book_isbn):
            self.book_dict[book_isbn].is_available = False
            self.book_dict[book_isbn].owner = user_id
            return True
        else:
            # log error
            return False

    def return_a_book(self, book_isbn: str):
        if self.is_book_in_db(book_isbn) and not self.is_book_available(book_isbn):
            self.book_dict[book_isbn].is_available = True
            self.book_dict[book_isbn].owner = "0"
            return True
        else:
            # log error
            return False
