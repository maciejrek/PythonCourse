import sys

sys.path.append('../')
import unittest
import book_category


class TestBookCategory(unittest.TestCase):

    def test_book_category_init(self):
        bc = book_category.BookCategory("TestCategory", "0")
        self.assertEqual(bc.name, "TestCategory")
        self.assertEqual(bc.id, "0")

    def test_book_category_prepare_to_json(self):
        bc = book_category.BookCategory("TestCategory", "0")
        bc_str = bc.prepare_to_json()
        self.assertEqual(bc_str['name'], "TestCategory")
