import sys

sys.path.append('../')
import os
import unittest
import users_database
import user
import json


def ret_test_dic():
    dic = dict()
    dic["0"] = {'name': "FirstUsersName", 'surname': "FirstUsersSurname"}
    dic["1"] = {'name': "SecondUsersName", 'surname': "SecondUsersSurname"}
    return dic


def prepare_db_file():
    dic = ret_test_dic()
    with open('udb_test.json', 'w') as file:
        json.dump(dic, file, indent=2)


def remove_db_file():
    if os.path.exists('udb_test.json'):
        os.remove('udb_test.json')


class TestUserDatabase(unittest.TestCase):

    def test_users_database_init_no_db_file(self):
        remove_db_file()
        db = users_database.UserDataBase('udb_test.json')
        self.assertEqual(db.user_dict, dict())

    def test_users_database_init(self):
        prepare_db_file()
        db = users_database.UserDataBase('udb_test.json')
        dic = ret_test_dic()
        for i in dic:
            self.assertEqual(db.user_dict[i].usr_id, i)
            self.assertEqual(db.user_dict[i].usr_name, dic[i]['name'])
            self.assertEqual(db.user_dict[i].usr_surname, dic[i]['surname'])
        remove_db_file()

    def test_is_user_in_db(self):
        prepare_db_file()
        db = users_database.UserDataBase('udb_test.json')
        self.assertTrue(db.is_user_in_db("0"))
        self.assertFalse(db.is_user_in_db("7"))
        remove_db_file()

    def test_add_user(self):
        prepare_db_file()
        db = users_database.UserDataBase('udb_test.json')
        self.assertFalse(db.is_user_in_db("7"))
        usr = user.User("7", "Test", "User")
        self.assertTrue(db.add_user(usr))
        self.assertTrue(db.is_user_in_db("7"))
        remove_db_file()

    def test_remove_user(self):
        prepare_db_file()
        db = users_database.UserDataBase('udb_test.json')
        self.assertFalse(db.is_user_in_db("7"))
        usr = user.User("7", "Test", "User")
        self.assertTrue(db.add_user(usr))
        self.assertTrue(db.is_user_in_db("7"))
        self.assertTrue(db.remove_user(usr.usr_id))
        self.assertFalse(db.is_user_in_db("7"))
        remove_db_file()

    def test_return_user_list(self):
        prepare_db_file()
        db = users_database.UserDataBase('udb_test.json')
        usr_list = db.return_list()
        temp_list = [db.user_dict["0"].usr_name + " " + db.user_dict["0"].usr_surname,
                     db.user_dict["1"].usr_name + " " + db.user_dict["1"].usr_surname]
        self.assertEqual(usr_list, temp_list)
        remove_db_file()

    def test_return_max_id(self):
        prepare_db_file()
        db = users_database.UserDataBase('udb_test.json')
        self.assertEqual("1", db.get_max_id())
        remove_db_file()
