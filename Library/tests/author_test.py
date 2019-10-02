import sys

sys.path.append('../')
import unittest
import author


class TestAuthor(unittest.TestCase):

    def test_author_init(self):
        aut = author.Author("0", "AuthorsName", "AuthorsSurname")
        self.assertEqual(aut.uid, "0")
        self.assertEqual(aut.aut_name, "AuthorsName")
        self.assertEqual(aut.aut_surname, "AuthorsSurname")

    def test_author_prepare_to_json(self):
        aut = author.Author("0", "AuthorsName", "AuthorsSurname")
        dic = aut.prepare_to_json()
        self.assertEqual(dic['name'], "AuthorsName")
        self.assertEqual(dic['surname'], "AuthorsSurname")
