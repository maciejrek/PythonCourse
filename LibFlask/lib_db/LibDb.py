import mysql.connector as mc
import logging
from time import sleep
from datetime import datetime


class LibDb:
    def __init__(self, host: str, user: str, passwd: str, database: str = None):
        self.db_exists = False
        self.db = self.connect(host, user, passwd, database)
        self.cursor = self.db.cursor(buffered=True)

    def create_db(self, name: str):
        self.execute(f"CREATE DATABASE IF NOT EXISTS {name}")

    def remove_db(self, name: str):
        self.execute(f"DROP DATABASE IF EXISTS {name}")

    def execute(self, query: str):
        self.cursor.execute(query)

    def response(self):
        return self.cursor.fetchall()

    def response_single(self):
        return self.cursor.fetchone()

    def show_columns(self, name: str):
        self.execute(f"SHOW columns FROM {name}")
        temp = self.response()
        print(f"\nshow_columns method - delete me please\n{name}\n")
        for i in temp:
            print(i)
        return temp

    def remove_table(self, name: str):
        self.execute(f'"DROP TABLE IF EXISTS {name}"')

    def show_db(self):
        self.execute("SHOW DATABASES")
        print("show_db method - delete me please")
        for i in self.cursor:
            print(i)

    def connect(self, host: str, user: str, passwd: str, database: str = None):
        if not database:
            logging.info("Connecting to server")
            return mc.connect(host=host, user=user, passwd=passwd)
        else:
            logging.info("Connecting to database")
            self.db_exists = True
            return mc.connect(host=host, user=user, passwd=passwd, database=database)

    def prepare_db(self, name: str):
        self.create_db(name)
        self.execute(f"USE {name}")
        logging.info("Creating USER table")
        self.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL,"
                     "surname VARCHAR(255) NOT NULL, active TINYINT(1) DEFAULT 1)")
        logging.info("Creating AUTHOR table")
        self.execute("CREATE TABLE author (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL,"
                     "surname VARCHAR(255) NOT NULL, active TINYINT(1) DEFAULT 1)")
        logging.info("Creating CATEGORY table")
        self.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, "
                     "active TINYINT(1) DEFAULT 1)")
        logging.info("Creating BOOK table")
        self.execute("CREATE TABLE book("
                     "id int NOT NULL AUTO_INCREMENT, "
                     "title varchar(255) NOT NULL, "
                     "id_author int NOT NULL, "
                     "id_category int NOT NULL, "
                     "isbn int NOT NULL,"
                     "active TINYINT(1) DEFAULT 1,"
                     " PRIMARY KEY(id), "
                     "FOREIGN KEY(id_author) REFERENCES author(id), "
                     "FOREIGN KEY(id_category) REFERENCES category(id))")
        logging.info("Creating HISTORY table")
        self.execute("CREATE TABLE history("
                     "id int NOT NULL AUTO_INCREMENT, "
                     "id_book int NOT NULL, "
                     "id_user int NOT NULL, "
                     "time_borrow DATETIME NOT NULL DEFAULT '1990-01-01 00:00:00', "
                     "time_return DATETIME NOT NULL DEFAULT '1990-01-01 00:00:00', "
                     " PRIMARY KEY(id), "
                     "FOREIGN KEY(id_book) REFERENCES book(id), "
                     "FOREIGN KEY(id_user) REFERENCES user(id))")

    def add_user(self, name: str, surname: str):
        self.cursor.execute(f"INSERT INTO user (name, surname) VALUES ('{name}','{surname}')")
        self.db.commit()
        return self.cursor.lastrowid

    def add_users(self, usr: list):
        self.cursor.executemany("INSERT INTO user (name, surname) VALUES (%s,%s)", usr)
        self.db.commit()

    def add_author(self, name: str, surname: str):
        self.cursor.execute(f"INSERT INTO author (name, surname) VALUES ('{name}','{surname}')")
        self.db.commit()
        return self.cursor.lastrowid

    def add_authors(self, auth: list):
        self.cursor.executemany("INSERT INTO author (name, surname) VALUES (%s,%s)", auth)
        self.db.commit()

    def add_category(self, cat: str):
        self.cursor.execute(f"INSERT INTO category (name) VALUES ('{cat}')")
        self.db.commit()
        return self.cursor.lastrowid

    def add_categories(self, cat: list):
        self.cursor.executemany("INSERT INTO category (name) VALUES (%s)", cat)
        self.db.commit()

    def add_book(self, title: str, auth: int, cat: int, isbn: int):
        self.cursor.execute(
            f"INSERT INTO book (title,id_author,id_category,isbn) VALUES ('{title}',{auth},{cat},{isbn})")
        self.db.commit()
        return self.cursor.lastrowid

    def add_history_entry(self, book_id: int, user_id: int, time_in: str):
        self.cursor.execute(
            f"INSERT INTO history(id_book,id_user,time_borrow) VALUES ({book_id},{user_id}, '{time_in}')")
        self.db.commit()
        return self.cursor.lastrowid

    def update_history_entry(self, book_id: int, time_out: str):
        self.cursor.execute(f"UPDATE history SET time_return = '{time_out}' WHERE id_book = '{book_id}' AND "
                            f"time_return = '1990-01-01 00:00:00'")

    def remove_entry(self, tab: str, entry_id: int):
        self.execute(f"DELETE FROM {tab} WHERE id = {entry_id}")
        self.db.commit()
        return self.cursor.rowcount

    def set_inactive(self, tab: str, entry_id: int):
        self.execute(f"UPDATE {tab} SET active = 0 WHERE id = {entry_id}")
        self.db.commit()

    def set_active(self, tab: str, entry_id: int):
        self.execute(f"UPDATE {tab} SET active = 1 WHERE id = {entry_id}")
        self.db.commit()

    def return_single_row_detailed(self, tab: str, entry_id: int):
        self.execute(f"SELECT * FROM {tab} WHERE id={entry_id}")
        return self.response_single()

    def return_single_row(self, params: list, tab: str, entry_id: int):
        self.execute(f'SELECT {",".join(params)} FROM {tab} WHERE id={entry_id}')
        return self.response_single()

    def return_tab(self, tab: str):
        self.execute(f"SELECT * FROM {tab}")
        return self.response()

    def return_tab_by_param(self, param: str, tab: str):
        self.execute(f"SELECT {param} FROM {tab}")
        return self.response()

    def return_tab_by_category(self, tab: str, cat: str, param: str):
        self.execute(f"SELECT * from {tab} where {cat} = '{param}'")
        return self.response()

    def borrow_a_book(self, book_id: int, user_id: int):
        return self.add_history_entry(book_id, user_id, datetime.now())

    def return_a_book(self, book_id: int):
        self.update_history_entry(book_id, datetime.now())

    def return_inactive(self):
        book = self.return_tab_by_category("book", "active", 0)
        cat = self.return_tab_by_category("category", "active", 0)
        user = self.return_tab_by_category("user", "active", 0)
        author = self.return_tab_by_category("author", "active", 0)
        ret_dict = {"book": list(), "category": list(), "user": list(), "author": list()}
        for i in book:
            uid, _, _, _, _, _ = i
            ret_dict["book"].append(uid)
        for i in cat:
            uid, _, _ = i
            ret_dict["category"].append(uid)
        for i in user:
            uid, _, _, _ = i
            ret_dict["user"].append(uid)
        for i in author:
            uid, _, _, _ = i
            ret_dict["author"].append(uid)
        return ret_dict


def prepare_database(name: str):
    lib = LibDb("localhost", "root", "root")
    while 1:
        try:
            lib.execute(f"USE {name}")
            logging.info("Connected")
            break
        except mc.Error as err:
            if err.errno == mc.errorcode.ER_BAD_DB_ERROR:
                logging.error(f"{err.msg}!")
                lib.prepare_db(name)
                sleep(1)
                break
            else:
                logging.error(f"ERROR {err.msg}!")
                sleep(1)
    return lib
