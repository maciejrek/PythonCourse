import sys

sys.path.append('../')
import os
import unittest
import book_database
import my_book
import json


def ret_test_dic():
    dic = dict()
    dic["787272"] = {'title': "FirstTitle", 'author': "0", 'isbn': "787272", 'owner': "0", 'category': "0",
                     'availability': True}
    dic["363535"] = {'title': "SecondTitle", 'author': "1", 'isbn': "363535", 'owner': "2", 'category': "2",
                     'availability': False}
    return dic


def prepare_db_file():
    dic = ret_test_dic()
    with open('bdb_test.json', 'w') as file:
        json.dump(dic, file, indent=2)


def remove_db_file():
    if os.path.exists('bdb_test.json'):
        os.remove('bdb_test.json')


class TestBookDatabase(unittest.TestCase):

    def test_book_database_init_no_db_file(self):
        remove_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertEqual(db.book_dict, dict())

    def test_book_database_init(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        dic = ret_test_dic()
        for i in dic:
            self.assertEqual(db.book_dict[i].isbn, i)
            self.assertEqual(db.book_dict[i].author, dic[i]['author'])
            self.assertEqual(db.book_dict[i].owner, dic[i]['owner'])
            self.assertEqual(db.book_dict[i].author, dic[i]['author'])
            self.assertEqual(db.book_dict[i].category, dic[i]['category'])
            self.assertEqual(db.book_dict[i].title, dic[i]['title'])
            self.assertEqual(db.book_dict[i].is_available, dic[i]['availability'])
        remove_db_file()

    def test_is_book_in_db(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertTrue(db.is_book_in_db("787272"))
        self.assertFalse(db.is_book_in_db("111111"))
        remove_db_file()

    def test_add_book(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertFalse(db.is_book_in_db("422429"))
        bc = my_book.MyBook("2", "TestTitle", "422429", "2", )
        self.assertTrue(db.add_book(bc))
        self.assertTrue(db.is_book_in_db("422429"))
        remove_db_file()

    def test_remove_book(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertFalse(db.is_book_in_db("422429"))
        bc = my_book.MyBook("2", "TestTitle", "422429", "2", )
        self.assertTrue(db.add_book(bc))
        self.assertTrue(db.is_book_in_db("422429"))
        self.assertTrue(db.remove_book("422429"))
        self.assertFalse(db.is_book_in_db("422429"))
        remove_db_file()

    def test_return_dict_by_author(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        temp_dict = dict()
        for i in db.book_dict:
            temp_dict[db.book_dict[i].author] = db.book_dict[i].title

        aut_dict,pointless_list = db.return_dict_by_author()
        self.assertEqual(temp_dict, aut_dict)
        remove_db_file()

    def test_return_dict_by_category(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        bc = my_book.MyBook("2", "TestTitle", "422429", "2", )
        db.add_book(bc)
        temp_dict = dict()
        temp_dict["0"] = ["FirstTitle"]
        temp_dict["2"] = ["SecondTitle", "TestTitle"]
        cat_dict = db.return_dict_by_category()
        self.assertEqual(temp_dict, cat_dict)
        self.assertEqual(len(cat_dict["0"]), 1)
        self.assertEqual(len(cat_dict["2"]), 2)
        remove_db_file()

    def test_loan_book(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertTrue(db.loan_book("787272", "5"))
        self.assertFalse(db.book_dict["787272"].is_available)
        self.assertEqual(db.book_dict["787272"].owner, "5")
        remove_db_file()

    def test_loan_book_no_book_negative(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertFalse(db.is_book_in_db("333333"))
        self.assertFalse(db.loan_book("333333", "5"))
        remove_db_file()

    def test_loan_book_not_available_negative(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        db.book_dict["787272"].is_available = False
        self.assertFalse(db.is_book_available("787272"))
        self.assertFalse(db.loan_book("787272", "5"))
        remove_db_file()

    def test_return_book(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        db.loan_book("787272", "5")
        self.assertFalse(db.book_dict["787272"].is_available)
        self.assertEqual(db.book_dict["787272"].owner, "5")
        self.assertTrue(db.return_a_book("787272"))
        self.assertTrue(db.book_dict["787272"].is_available)
        self.assertEqual(db.book_dict["787272"].owner, "0")
        remove_db_file()

    def test_return_book_no_book_negative(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertFalse(db.is_book_in_db("333333"))
        self.assertFalse(db.return_a_book("333333"))
        remove_db_file()

    def test_return_book_available_negative(self):
        prepare_db_file()
        db = book_database.BookDataBase('bdb_test.json')
        self.assertTrue(db.is_book_available("787272"))
        self.assertFalse(db.return_a_book("787272"))
        remove_db_file()
