import sys

sys.path.append('../')
import unittest
import user


class TestUser(unittest.TestCase):

    def test_user_init(self):
        usr = user.User("0", "UserName", "UserSurname")
        self.assertEqual(usr.usr_id, "0")
        self.assertEqual(usr.usr_name, "UserName")
        self.assertEqual(usr.usr_surname, "UserSurname")

    def test_user_prepare_to_json(self):
        usr = user.User("0", "UserName", "UserSurname")
        dic = usr.prepare_to_json()
        self.assertEqual(dic['name'], "UserName")
        self.assertEqual(dic['surname'], "UserSurname")
