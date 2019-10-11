import sys

sys.path.append('../')
import unittest
from lib_db import LibDb as db
from lib_db import book_db


class TestBookDatabase(unittest.TestCase):
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

    def tearDown(self) -> None:
        self.lib.remove_db("TestDatabase")

    def test_get_book_dict(self):
        book_dict = book_db.get_book_dict(self.lib)
        self.assertEqual(book_dict[1].uid, 1)
        self.assertEqual(book_dict[1].author, 1)
        self.assertEqual(book_dict[1].title, "FirstTitle")
        self.assertEqual(book_dict[1].isbn, 123123)
        self.assertEqual(book_dict[1].category, 1)
        self.assertEqual(book_dict[1].book_is_active, 1)
        self.assertEqual(book_dict[2].uid, 2)
        self.assertEqual(book_dict[2].author, 2)
        self.assertEqual(book_dict[2].title, "SecondTitle")
        self.assertEqual(book_dict[2].isbn, 414141)
        self.assertEqual(book_dict[2].category, 1)
        self.assertEqual(book_dict[2].book_is_active, 1)

    def test_get_book_dict_by_cat(self):
        book_dict = book_db.get_book_dict_by_cat(self.lib)
        self.assertEqual(book_dict[1], ["FirstTitle", "SecondTitle"])

    def test_get_book_list(self):
        book_list, book_id_list = book_db.get_book_list(self.lib)
        self.assertEqual(book_list, ['FirstTitle', 'SecondTitle'])
        self.assertEqual(book_id_list, [1, 2])

    def test_active_deactive(self):
        book_db.deactivate_book(self.lib, 2)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [2], "user": [], "category": [], "author": []})
        book_db.activate_book(self.lib, 2)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [], "category": [], "author": []})
