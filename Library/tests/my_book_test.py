import sys

sys.path.append('../')
import unittest
import my_book


class TestMyBook(unittest.TestCase):

    def test_my_book_init_default_params(self):
        bk = my_book.MyBook("0", "BooksTitle", "123456", "2")
        self.assertEqual(bk.author, "0")
        self.assertEqual(bk.title, "BooksTitle")
        self.assertEqual(bk.isbn, "123456")
        self.assertEqual(bk.category, "2")
        self.assertEqual(bk.owner, "0")
        self.assertEqual(bk.is_available, True)

    def test_my_book_init_custom_params(self):
        bk = my_book.MyBook("0", "BooksTitle", "123456", "2", "1", False)
        self.assertEqual(bk.author, "0")
        self.assertEqual(bk.title, "BooksTitle")
        self.assertEqual(bk.isbn, "123456")
        self.assertEqual(bk.category, "2")
        self.assertEqual(bk.owner, "1")
        self.assertEqual(bk.is_available, False)

    def test_my_book_prepare_to_json(self):
        bk = my_book.MyBook("0", "BooksTitle", "123456", "2")
        dic = bk.prepare_to_json()
        self.assertEqual(dic['title'], "BooksTitle")
        self.assertEqual(dic['author'], "0")
        self.assertEqual(dic['isbn'], "123456")
        self.assertEqual(dic['owner'], "0")
        self.assertEqual(dic['availability'], True)
