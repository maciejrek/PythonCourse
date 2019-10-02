from typing import Iterable, Dict

import author
import json


class AuthorDataBase:
    """
    Author database, with the following properties:

    Attributes:
    """

    def __init__(self, file_name: str):
        self.save_directory = file_name
        self.load_directory = file_name
        self.author_dict: Dict[str, author.Author] = self.load_author()

    def load_author(self):
        try:
            with open(self.load_directory, 'r') as file:
                # logger : loading data from file
                x = json.load(file)
                temp_dict = dict()
                for i in x:
                    temp_dict[i] = author.Author(i, x[i]['name'], x[i]['surname'])
                return temp_dict
        except FileNotFoundError:
            # logger : file does not exist
            return dict()

    def save_author(self):
        dic = dict()
        for i in self.author_dict:
            dic[i] = self.author_dict[i].prepare_to_json()
        with open(self.save_directory, 'w') as file:
            json.dump(dic, file, indent=2)

    # uid as param cause i assume programmer know what he's doing
    def is_author_in_db(self, uid: int):
        for i in self.author_dict:
            if i == uid:
                return True
        return False

    def add_author(self, aut: author.Author):
        if not self.is_author_in_db(aut.uid):
            self.author_dict[aut.uid] = aut
            # logger : user added
            return True
        return False

    def remove_author(self, uid: str):
        if self.is_author_in_db(uid):
            del self.author_dict[uid]
        return True

    def return_list(self):
        temp = list()
        for i in self.author_dict:
            temp.append(self.author_dict[i].aut_name + " " + self.author_dict[i].aut_surname)
        return temp

    def get_id(self, aut:str):
        for i in self.author_dict:
            if self.author_dict[i].aut_name + " " + self.author_dict[i].aut_surname == aut:
                return self.author_dict[i].uid

    def get_max_id(self):
        return max(self.author_dict.keys())
    # DONE FOR NOW
