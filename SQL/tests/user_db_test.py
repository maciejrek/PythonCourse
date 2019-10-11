import sys

sys.path.append('../')
import unittest
from lib_db import LibDb as db
from lib_db import user_db


class TestUserDatabase(unittest.TestCase):
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

    def test_get_user_dict(self):
        usr_dict = user_db.get_user_dict(self.lib)

        self.assertEqual(usr_dict[1].usr_id, 1)
        self.assertEqual(usr_dict[1].usr_name, "First")
        self.assertEqual(usr_dict[1].usr_surname, "User")
        self.assertEqual(usr_dict[1].usr_is_active, 1)
        self.assertEqual(usr_dict[2].usr_id, 2)
        self.assertEqual(usr_dict[2].usr_name, "Second")
        self.assertEqual(usr_dict[2].usr_surname, "User")
        self.assertEqual(usr_dict[2].usr_is_active, 1)

    def test_get_user_list(self):
        usr_list, usr_id_list = user_db.get_user_list(self.lib)
        self.assertEqual(usr_list, ['First User', 'Second User'])
        self.assertEqual(usr_id_list, [1, 2])

    def test_active_deactive(self):
        user_db.deactivate_user(self.lib, 2)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [2], "category": [], "author": []})
        user_db.activate_user(self.lib, 2)
        inactive = self.lib.return_inactive()
        self.assertEqual(inactive, {"book": [], "user": [], "category": [], "author": []})
