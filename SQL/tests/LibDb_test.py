import sys

sys.path.append('../')
import unittest
from lib_db import LibDb as db
import datetime


class TestSqlDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.lib = db.LibDb("localhost", "root", "root")
        self.lib.prepare_db("TestDatabase")

    def tearDown(self) -> None:
        self.lib.remove_db("TestDatabase")

    def test_add_user(self):
        """ Test add single user functionality """
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        self.assertEqual(self.lib.add_user("First", "User"), 1)
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "User", 1))

    def test_add_users(self):
        """ Test add multiple users functionality """
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchall(), [])
        self.lib.add_users([("First", "User"), ("Second", "User")])
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchall(), [(1, "First", "User", 1), (2, "Second", "User", 1)])

    def test_add_author(self):
        """ Test add single author functionality """
        self.lib.execute("SELECT * FROM author")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        self.lib.add_author("First", "Author")
        self.lib.execute("SELECT * FROM author")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "Author", 1))

    def test_add_authors(self):
        """ Test add multiple authors functionality """
        self.lib.execute("SELECT * FROM author")
        self.assertEqual(self.lib.cursor.fetchall(), [])
        self.lib.add_authors([("First", "Author"), ("Second", "Author")])
        self.lib.execute("SELECT * FROM author")
        self.assertEqual(self.lib.cursor.fetchall(), [(1, "First", "Author", 1), (2, "Second", "Author", 1)])

    def test_add_category(self):
        """ Test add single category functionality """
        self.lib.execute("SELECT * FROM category")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        self.lib.add_category("Name")
        self.lib.execute("SELECT * FROM category")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "Name", 1))

    def test_add_categories(self):
        """ Test add multiple categories functionality """
        self.lib.execute("SELECT * FROM category")
        self.assertEqual(self.lib.cursor.fetchall(), [])
        self.lib.add_categories([("First",), ("Second",)])
        self.lib.execute("SELECT * FROM category")
        self.assertEqual(self.lib.cursor.fetchall(), [(1, "First", 1), (2, "Second", 1)])

    def test_add_book(self):
        """ Test add single book functionality """
        self.lib.execute("SELECT * FROM book")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        ''' Adding Author and Category, because they're needed to add book '''
        self.lib.add_author("First", "Author")
        self.lib.add_category("Name")
        self.lib.add_book("title", 1, 1, 123123)
        self.lib.execute("SELECT * FROM book")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "title", 1, 1, 123123, 1))

    def test_add_history_entry(self):
        """ Test add single history entry (simulate borrowing book) functionality """
        self.lib.execute("SELECT * FROM history")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        ''' Adding User, Author, Category and Book to test History module '''
        self.lib.add_author("First", "Author")
        self.lib.add_category("Name")
        self.lib.add_book("title", 1, 1, 123123)
        self.lib.add_user("First", "User")
        self.lib.add_history_entry(1, 1, datetime.datetime(2000, 10, 10, 11, 22))
        self.lib.execute("SELECT * FROM history")
        self.assertEqual(self.lib.cursor.fetchone(),
                         (1, 1, 1, datetime.datetime(2000, 10, 10, 11, 22), datetime.datetime(1990, 1, 1, 0, 0)))

    def test_update_history_entry(self):
        """ Test update single history entry (simulate returning book) functionality """
        self.lib.execute("SELECT * FROM history")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        ''' Adding User, Author, Category and Book to test History module '''
        self.lib.add_author("First", "Author")
        self.lib.add_category("Name")
        self.lib.add_book("title", 1, 1, 123123)
        self.lib.add_user("First", "User")
        self.lib.add_history_entry(1, 1, datetime.datetime(2000, 10, 10, 11, 22))
        self.lib.execute("SELECT * FROM history")
        self.assertEqual(self.lib.cursor.fetchone(),
                         (1, 1, 1, datetime.datetime(2000, 10, 10, 11, 22), datetime.datetime(1990, 1, 1, 0, 0)))
        self.lib.update_history_entry(1, datetime.datetime(2010, 7, 20, 8, 7))
        self.lib.execute("SELECT * FROM history")
        self.assertEqual(self.lib.cursor.fetchone(),
                         (1, 1, 1, datetime.datetime(2000, 10, 10, 11, 22), datetime.datetime(2010, 7, 20, 8, 7)))

    def test_update_multiple_history_entry(self):
        """ Test update single history entry, with 2 entries (simulate returning one book) functionality """
        self.lib.execute("SELECT * FROM history")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        ''' Adding User, Author, Category and Book to test History module '''
        self.lib.add_author("First", "Author")
        self.lib.add_author("Second", "Author")
        self.lib.add_category("FirstCat")
        self.lib.add_category("SecondCat")
        self.lib.add_book("FirstTitle", 1, 1, 123123)
        self.lib.add_book("SecondTitle", 2, 2, 246246)
        self.lib.add_user("First", "User")
        self.lib.add_user("Second", "User")
        self.lib.add_history_entry(1, 1, datetime.datetime(2000, 10, 10, 11, 22))
        self.lib.add_history_entry(2, 2, datetime.datetime(2000, 11, 11, 7, 7))
        self.lib.execute("SELECT * FROM history")
        resp = self.lib.cursor.fetchall()
        self.assertEqual(resp[0],
                         (1, 1, 1, datetime.datetime(2000, 10, 10, 11, 22), datetime.datetime(1990, 1, 1, 0, 0)))
        self.assertEqual(resp[1],
                         (2, 2, 2, datetime.datetime(2000, 11, 11, 7, 7), datetime.datetime(1990, 1, 1, 0, 0)))
        self.lib.update_history_entry(2, datetime.datetime(2010, 7, 20, 8, 7))
        self.lib.execute("SELECT * FROM history")
        resp = self.lib.cursor.fetchall()
        self.assertEqual(resp[0],
                         (1, 1, 1, datetime.datetime(2000, 10, 10, 11, 22), datetime.datetime(1990, 1, 1, 0, 0)))
        self.assertEqual(resp[1],
                         (2, 2, 2, datetime.datetime(2000, 11, 11, 7, 7), datetime.datetime(2010, 7, 20, 8, 7)))

    def test_remove_entry(self):
        """ Test remove entry functionality for 2 random tables """

        self.lib.add_user("First", "User")
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "User", 1))
        self.lib.add_author("First", "Author")
        self.lib.execute("SELECT * FROM author")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "Author", 1))

        self.lib.remove_entry("user", 1)
        self.lib.remove_entry("author", 1)
        self.lib.execute("SELECT * FROM author")
        self.assertEqual(self.lib.cursor.fetchone(), None)
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), None)

    def test_set_inactive(self):
        """ Test set inactive (simulate removing user from active users database) functionality """
        self.lib.add_user("First", "User")
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "User", 1))
        self.lib.set_inactive("user", 1)
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "User", 0))

    def test_set_active(self):
        """ Test set active (simulate adding user back to active users database) functionality """
        self.lib.add_user("First", "User")
        self.lib.set_inactive("user", 1)
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "User", 0))
        self.lib.set_active("user", 1)
        self.lib.execute("SELECT * FROM user")
        self.assertEqual(self.lib.cursor.fetchone(), (1, "First", "User", 1))

    def test_return_single_row_detailed(self):
        """ Test return single row from table with all available columns """
        self.lib.add_user("First", "User")
        self.assertEqual(self.lib.return_single_row_detailed("user", 1), (1, "First", "User", 1))

    def test_return_single_row(self):
        """ Test return single row from table with certain columns """
        self.lib.add_user("First", "User")
        self.assertEqual(self.lib.return_single_row(["surname"], "user", 1), ("User",))
        self.assertEqual(self.lib.return_single_row(["name", "surname"], "user", 1), ("First", "User"))

    def test_return_tab(self):
        """ Test return tab functionality """
        self.lib.add_user("First", "User")
        self.lib.execute("SELECT * FROM user")
        resp1 = self.lib.cursor.fetchall()
        resp2 = self.lib.return_tab("user")
        self.assertEqual(resp1, resp2)

    def test_return_tab_by_category(self):
        """ Test return tab by category functionality """
        self.lib.add_user("First", "User")
        self.lib.execute("SELECT * FROM user WHERE name = 'First' ")
        resp1 = self.lib.cursor.fetchall()
        resp2 = self.lib.return_tab_by_category("user", "name", "First")
        self.assertEqual(resp1, resp2)

    def test_return_by_param(self):
        """ Test return by param functionality """
        self.lib.add_user("First", "User")
        self.lib.execute("SELECT name FROM user")
        resp1 = self.lib.cursor.fetchall()
        resp2 = self.lib.return_tab_by_param("name", "user")
        self.assertEqual(resp1, resp2)

    def test_return_inactive(self):
        self.lib.add_user("First", "User")
        resp = self.lib.return_inactive()
        self.assertEqual(resp, {"book": [], "user": [], "category": [], "author": []})
        self.lib.set_inactive("user", 1)
        resp = self.lib.return_inactive()
        self.assertEqual(resp, {"book": [], "user": [1], "category": [], "author": []})

