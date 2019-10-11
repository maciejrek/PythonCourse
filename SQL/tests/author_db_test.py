import sys

sys.path.append('../')
import unittest
from lib_db import LibDb as db
from lib_db import author_db


class TestAuthorDatabase(unittest.TestCase):
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

    def test_get_author_dict(self):
        aut_dict = author_db.get_author_dict(self.lib)

        self.assertEqual(aut_dict[1].uid, 1)
        self.assertEqual(aut_dict[1].aut_name, "First")
        self.assertEqual(aut_dict[1].aut_surname, "Author")
        self.assertEqual(aut_dict[1].aut_is_active, 1)
        self.assertEqual(aut_dict[2].uid, 2)
        self.assertEqual(aut_dict[2].aut_name, "Second")
        self.assertEqual(aut_dict[2].aut_surname, "Author")
        self.assertEqual(aut_dict[2].aut_is_active, 1)

    def test_get_author_list(self):
        aut_list, aut_id_list = author_db.get_author_list(self.lib)
        self.assertEqual(aut_list, ['First Author', 'Second Author'])
        self.assertEqual(aut_id_list, [1, 2])

    def test_active_deactive(self):
        author_db.deactivate_author(self.lib, 2)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [], "category": [], "author": [2]})
        author_db.activate_author(self.lib, 2)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [], "category": [], "author": []})
