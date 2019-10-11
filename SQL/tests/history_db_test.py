import sys

sys.path.append('../')
import unittest
from lib_db import LibDb as db
from lib_db import history_db
import datetime
import time


class TestHistoryDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.lib = db.LibDb("localhost", "root", "root")
        self.lib.prepare_db("TestDatabase")
        self.lib.add_user("First", "User")
        self.lib.add_user("Second", "User")
        self.lib.add_author("First", "Author")
        self.lib.add_author("Second", "Author")
        self.lib.add_category("FirstCategory")
        self.lib.add_book("FirstTitle", 1, 1, 123123)
        self.lib.add_book("SecondTitle", 2, 1, 414141)
        history_db.borrow_a_book(self.lib, 1, 1)
        history_db.borrow_a_book(self.lib, 2, 2)
        time.sleep(1)
        history_db.return_a_book(self.lib, 2)

    def tearDown(self) -> None:
        self.lib.remove_db("TestDatabase")

    def test_get_history_dict(self):
        hist_dict = history_db.get_history_dict(self.lib)
        self.assertEqual(hist_dict[1].uid, 1)
        self.assertEqual(hist_dict[1].book_id, 1)
        self.assertEqual(hist_dict[1].user_id, 1)
        self.assertNotEqual(hist_dict[1].date_in, datetime.datetime(1990, 1, 1, 0, 0))
        self.assertEqual(hist_dict[1].date_out, datetime.datetime(1990, 1, 1, 0, 0))

        self.assertEqual(hist_dict[2].uid, 2)
        self.assertEqual(hist_dict[2].book_id, 2)
        self.assertEqual(hist_dict[2].user_id, 2)
        self.assertNotEqual(hist_dict[2].date_in, datetime.datetime(1990, 1, 1, 0, 0))
        self.assertNotEqual(hist_dict[2].date_out, datetime.datetime(1990, 1, 1, 0, 0))

    def test_get_history_dict_by_user(self):
        hist_dict = history_db.get_history_dict_by_user(self.lib)
        self.assertEqual(hist_dict, {1: [1], 2: [2]})

    def test_get_history_dict_by_category(self):
        hist_dict = history_db.get_history_dict_by_book(self.lib)
        self.assertEqual(hist_dict, {1: [1], 2: [2]})

    def test_get_history_list_by_user(self):
        usr1 = history_db.get_history_list_by_user(self.lib, 1)
        usr2 = history_db.get_history_list_by_user(self.lib, 2)
        self.assertEqual(usr1, [1])
        self.assertEqual(usr2, [2])

    def test_get_history_list_by_book(self):
        book1 = history_db.get_history_list_by_book(self.lib, 1)
        book2 = history_db.get_history_list_by_book(self.lib, 2)
        self.assertEqual(book1, [1])
        self.assertEqual(book2, [2])

    def test_get_book_status(self):
        self.assertTrue(history_db.get_book_status(self.lib, 2))
        self.assertFalse(history_db.get_book_status(self.lib, 1))
