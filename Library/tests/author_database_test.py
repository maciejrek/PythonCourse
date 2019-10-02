import sys

sys.path.append('../')
import os
import unittest
import author_database
import author
import json


def ret_test_dic():
    dic = dict()
    dic["0"] = {'name': "FirstAuthorsName", 'surname': "FirstAuthorsSurname"}
    dic["1"] = {'name': "SecondAuthorsName", 'surname': "SecondAuthorsSurname"}
    return dic


def prepare_db_file():
    dic = ret_test_dic()
    with open('adb_test.json', 'w') as file:
        json.dump(dic, file, indent=2)


def remove_db_file():
    if os.path.exists('adb_test.json'):
        os.remove('adb_test.json')


class TestAuthorDatabase(unittest.TestCase):

    def test_author_database_init_no_db_file(self):
        remove_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        self.assertEqual(db.author_dict, dict())

    def test_author_database_init(self):
        prepare_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        dic = ret_test_dic()
        for i in dic:
            self.assertEqual(db.author_dict[i].uid, i)
            self.assertEqual(db.author_dict[i].aut_name, dic[i]['name'])
            self.assertEqual(db.author_dict[i].aut_surname, dic[i]['surname'])
        remove_db_file()

    def test_is_author_in_db(self):
        prepare_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        self.assertTrue(db.is_author_in_db("0"))
        self.assertFalse(db.is_author_in_db("7"))
        remove_db_file()

    def test_add_author(self):
        prepare_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        self.assertFalse(db.is_author_in_db("7"))
        aut = author.Author("7", "Test", "User")
        self.assertTrue(db.add_author(aut))
        self.assertTrue(db.is_author_in_db("7"))
        remove_db_file()

    def test_remove_author(self):
        prepare_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        self.assertFalse(db.is_author_in_db("7"))
        aut = author.Author("7", "Test", "User")
        self.assertTrue(db.add_author(aut))
        self.assertTrue(db.is_author_in_db("7"))
        self.assertTrue(db.remove_author(aut.uid))
        self.assertFalse(db.is_author_in_db("7"))
        remove_db_file()

    def test_return_author_list(self):
        prepare_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        aut_list = db.return_list()
        temp_list = [db.author_dict["0"].aut_name + " " + db.author_dict["0"].aut_surname,
                     db.author_dict["1"].aut_name + " " + db.author_dict["1"].aut_surname]
        self.assertEqual(aut_list, temp_list)
        remove_db_file()

    def test_return_max_id(self):
        prepare_db_file()
        db = author_database.AuthorDataBase('adb_test.json')
        self.assertEqual("1", db.get_max_id())
        remove_db_file()
