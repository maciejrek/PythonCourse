import sys

sys.path.append('../')
import unittest
from lib_db import LibDb as db
from lib_db import category_db


class TestCategoryDatabase(unittest.TestCase):
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

    def test_get_category_dict(self):
        cat_dict = category_db.get_category_dict(self.lib)

        self.assertEqual(cat_dict[1].uid, 1)
        self.assertEqual(cat_dict[1].name, "FirstCategory")
        self.assertEqual(cat_dict[1].cat_is_active, 1)

#
    def test_get_category_list(self):
        cat_list, cat_id_list = category_db.get_category_list(self.lib)
        self.assertEqual(cat_list, ['FirstCategory'])
        self.assertEqual(cat_id_list, [1])
#
    def test_active_deactive(self):
        category_db.deactivate_category(self.lib, 1)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [], "category": [1], "author": []})
        category_db.activate_category(self.lib, 1)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [], "category": [], "author": []})
