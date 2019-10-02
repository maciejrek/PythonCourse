from typing import Iterable, Dict

import book_category as bc
import json


class BookCategoryDataBase:
    """
    Book category database, with the following properties:

    Attributes:
    """

    def __init__(self, file_name: str):
        self.save_directory = file_name
        self.load_directory = file_name
        self.book_cat_dict: Dict[str, bc.BookCategory] = self.load_book_category()

    def load_book_category(self):
        try:
            with open(self.load_directory, 'r') as file:
                # logger : loading data from file
                x = json.load(file)
                temp_dict = dict()
                for i in x:
                    temp_dict[i] = bc.BookCategory(x[i]['name'], i)
                return temp_dict
        except FileNotFoundError:
            # logger : file does not exist
            return dict()

    def save_book_cat(self):
        dic = dict()
        for i in self.book_cat_dict:
            dic[i] = self.book_cat_dict[i].prepare_to_json()
        with open(self.save_directory, 'w') as file:
            json.dump(dic, file, indent=2)

    # id as param cause i assume programmer know what he's doing
    def is_book_cat_in_db(self, uid: str):
        for i in self.book_cat_dict:
            if i == uid:
                return True
        return False

    def add_book_cat(self, book_cat: bc.BookCategory):
        if not self.is_book_cat_in_db(book_cat.id):
            self.book_cat_dict[book_cat.id] = book_cat
            # logger : user added
            return True
        return False

    def remove_book_cat(self, bc_id: str):
        if self.is_book_cat_in_db(bc_id):
            del self.book_cat_dict[bc_id]
        return True

    def return_list(self):
        temp = list()
        for i in self.book_cat_dict:
            temp.append(self.book_cat_dict[i].name)
        return temp

    def get_id(self, book_cat: str):
        for i in self.book_cat_dict:
            if self.book_cat_dict[i].name == book_cat:
                return self.book_cat_dict[i].id

    def get_max_id(self):
        return max(self.book_cat_dict.keys())
