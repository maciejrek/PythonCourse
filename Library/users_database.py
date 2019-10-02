from typing import Iterable, Dict

import user
import json


class UserDataBase:
    """
    Users database, with the following properties:

    Attributes:
    """

    def __init__(self, file_name: str):
        self.save_directory = file_name
        self.load_directory = file_name
        self.user_dict: Dict[str, user.User] = self.load_users()

    def load_users(self):
        try:
            with open(self.load_directory, 'r') as file:
                # logger : loading data from file
                x = json.load(file)
                temp_dict = dict()
                for i in x:
                    temp_dict[i] = user.User(i, x[i]['name'], x[i]['surname'])
                return temp_dict
        except FileNotFoundError:
            # logger : file does not exist
            return dict()

    def save_users(self):
        dic = dict()
        for i in self.user_dict:
            dic[i] = self.user_dict[i].prepare_to_json()
        with open(self.save_directory, 'w') as file:
            json.dump(dic, file, indent=2)

    # uid as param cause i assume programmer know what he's doing
    def is_user_in_db(self, uid: str):
        for i in self.user_dict:
            if i == uid:
                return True
        return False

    def add_user(self, usr: user.User):
        if not self.is_user_in_db(usr.usr_id):
            self.user_dict[usr.usr_id] = usr
            # logger : user added
            return True
        return False

    def remove_user(self, usr_id: str):
        if self.is_user_in_db(usr_id):
            del self.user_dict[usr_id]
        return True

    def return_list(self):
        temp = list()
        for i in self.user_dict:
            temp.append(self.user_dict[i].usr_name + " " + self.user_dict[i].usr_surname)
        return temp

    def get_id(self, usr: str):
        for i in self.user_dict:
            if self.user_dict[i].usr_name + " " + self.user_dict[i].usr_surname == usr:
                return self.user_dict[i].usr_id

    def get_max_id(self):
        return max(self.user_dict.keys())
