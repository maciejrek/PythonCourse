import sys

sys.path.append('../')
import os
import unittest
import book_category_database
import book_category
import json


def ret_test_dic():
    dic = dict()
    dic["0"] = {'name': "FirstCategoryName"}
    dic["1"] = {'name': "SecondCategoryName"}
    return dic


def prepare_db_file():
    dic = ret_test_dic()
    with open('bcdb_test.json', 'w') as file:
        json.dump(dic, file, indent=2)


def remove_db_file():
    if os.path.exists('bcdb_test.json'):
        os.remove('bcdb_test.json')


class TestBookCategoryDatabase(unittest.TestCase):

    def test_book_category_database_init_no_db_file(self):
        remove_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        self.assertEqual(db.book_cat_dict, dict())

    def test_book_category_database_init(self):
        prepare_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        dic = ret_test_dic()
        for i in dic:
            self.assertEqual(db.book_cat_dict[i].id, i)
            self.assertEqual(db.book_cat_dict[i].name, dic[i]['name'])
        remove_db_file()

    def test_is_book_category_in_db(self):
        prepare_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        self.assertTrue(db.is_book_cat_in_db("0"))
        self.assertFalse(db.is_book_cat_in_db("7"))
        remove_db_file()

    def test_add_book_category(self):
        prepare_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        self.assertFalse(db.is_book_cat_in_db("7"))
        bc = book_category.BookCategory("Test", "7")
        self.assertTrue(db.add_book_cat(bc))
        self.assertTrue(db.is_book_cat_in_db("7"))
        remove_db_file()

    def test_remove_book_category(self):
        prepare_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        self.assertFalse(db.is_book_cat_in_db("7"))
        bc = book_category.BookCategory("Test", "7")
        self.assertTrue(db.add_book_cat(bc))
        self.assertTrue(db.is_book_cat_in_db("7"))
        self.assertTrue(db.remove_book_cat("7"))
        self.assertFalse(db.is_book_cat_in_db("7"))
        remove_db_file()

    def test_return_book_category_list(self):
        prepare_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        bc_list = db.return_list()
        temp_list = [db.book_cat_dict["0"].name, db.book_cat_dict["1"].name]
        self.assertEqual(bc_list, temp_list)
        remove_db_file()

    def test_return_max_id(self):
        prepare_db_file()
        db = book_category_database.BookCategoryDataBase('bcdb_test.json')
        self.assertEqual("1", db.get_max_id())
        remove_db_file()
