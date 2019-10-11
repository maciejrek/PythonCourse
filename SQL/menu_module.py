from mysql.connector import Error
import manager
import logging


class Menu(object):

    def __init__(self, menu_name: str, menu_list: list):
        self.name = menu_name
        self.list = menu_list

    def print_menu(self):
        print(self.name)
        if len(self.list) == 0:
            print("Empty!")
        for idx, i in enumerate(self.list):
            print(f"{idx}: {i}")


def prep_book_list(mgr: manager.LibraryManager):
    book_dict = mgr.get_book_dict(mgr.database)
    aut_dict = mgr.get_authors_dict(mgr.database)
    list_copy = list()
    for i in book_dict:
        list_copy.append(f"{book_dict[i].title} by {aut_dict[book_dict[i].author].fullname} ")
    list_copy.append('Exit')
    return list_copy


class MyApp:
    main_menu_l = ['Databases', 'Borrow a Book', 'Return Book', 'Add...', 'Remove...', 'Inactive', 'Exit']
    db_submenu_l = ['User database', 'Book database', 'Book category database', 'Author database', 'Exit']
    action_menu_l = ['Book', 'Author', 'User', 'Category', 'Exit']

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.main_menu = Menu("Main Menu", MyApp.main_menu_l)
        self.db_submenu = None
        self.loan_submenu = None
        self.return_submenu = None
        self.add_menu = None
        self.remove_menu = None

        mgr = manager.LibraryManager()

        while 1:
            self.main_menu.print_menu()
            key = input()
            if key == "0":
                self.prep_database_menu(mgr)
            elif key == "1":
                self.prep_borrow_menu(mgr)
            elif key == "2":
                self.prep_return_menu(mgr)
            elif key == "3":
                self.prep_add_menu(mgr)
            elif key == "4":
                self.prep_remove_menu(mgr)
            elif key == "5":
                self.prep_inactive_menu(mgr)
            else:
                print("Finishing program")
                break

    # DATABASE FUNCTIONALITY
    def prep_database_menu(self, mgr: manager.LibraryManager):
        pass
        self.db_submenu = Menu("Database Menu", MyApp.db_submenu_l)
        while 1:
            self.db_submenu.print_menu()
            key = input()
            if key == "0":
                self.prep_user_db(mgr)
            elif key == "1":
                self.prep_book_db(mgr)
            elif key == "2":
                self.prep_book_cat_db(mgr)
            elif key == "3":
                self.prep_author_db(mgr)
            elif key == str(len(MyApp.db_submenu_l) - 1):
                logging.info("Leaving submenu")
                break
            else:
                logging.error('Wrong Key')

    def prep_add_menu(self, mgr: manager.LibraryManager):
        self.add_menu = Menu("Add:", MyApp.action_menu_l)
        while 1:
            self.add_menu.print_menu()
            key = input()
            if key == "0":
                self.add_book(mgr)
            elif key == "1":
                self.add_author(mgr)
            elif key == "2":
                self.add_user(mgr)
            elif key == "3":
                self.add_book_cat(mgr)
            elif key == "4":
                logging.info("Leaving submenu")
                break
            else:
                logging.error("Wrong key!")

    def prep_remove_menu(self, mgr: manager.LibraryManager):
        self.remove_menu = Menu("Remove:", MyApp.action_menu_l)
        while 1:
            self.remove_menu.print_menu()
            key = input()
            if key == "0":
                self.rem_book(mgr)
            elif key == "1":
                self.rem_author(mgr)
            elif key == "2":
                self.rem_user(mgr)
            elif key == "3":
                self.rem_book_cat(mgr)
            elif key == "4":
                logging.info("Leaving submenu")
                break
            else:
                logging.error("Wrong key!")

    @staticmethod
    def prep_inactive_menu(mgr: manager.LibraryManager):
        temp_dict = mgr.database.return_inactive()
        while 1:
            print(temp_dict, "\nPress key to continue")
            input()
            break

    @staticmethod
    def prep_user_db(mgr: manager.LibraryManager):
        user_list, user_id_list = mgr.get_user_list(mgr.database)
        user_list.append('Exit')
        current_view = Menu("User Database Menu", user_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(user_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            elif int(key) < len(user_list):
                usr_list = mgr.get_history_list_by_user(mgr.database, user_id_list[int(key)])
                book_dict = mgr.get_book_dict(mgr.database)
                if not usr_list:
                    logging.info(f"No history for {user_list[int(key)]}, press key to return.")
                    input()
                else:
                    book_list = [book_dict[i].title for i in usr_list]
                    user_history_menu = Menu("User History Menu", book_list)
                    user_history_menu.print_menu()
                    logging.info("Press key to return")
                    input()
            else:
                logging.error("Wrong key!")

    @staticmethod
    def prep_book_cat_db(mgr: manager.LibraryManager):
        cat_list, cat_id_list = mgr.get_category_list(mgr.database)
        cat_list.append('Exit')
        current_view = Menu("Book Category Database Menu", cat_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(cat_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            elif int(key) < len(cat_list):
                by_cat = mgr.get_book_dict_by_cat(mgr.database)
                # +1 because list starts with 0, db with 1
                if int(key) + 1 not in cat_id_list and int(key) < len(cat_list):
                    logging.info('Empty!')
                    input()
                elif int(key) < len(cat_list):
                    if cat_id_list[int(key)] not in by_cat.keys():
                        logging.info(f"No history for {cat_list[int(key)]}, press key to continue")
                        input()
                        break
                    book_cat_list = Menu("Book Category List", by_cat[cat_id_list[int(key)]])
                    book_cat_list.print_menu()
                    input()
                else:
                    logging.error('Wrong Key')
                    break

    @staticmethod
    def prep_book_db(mgr: manager.LibraryManager):
        book_list, book_id_list = mgr.get_book_list(mgr.database)
        book_dict = mgr.get_book_dict(mgr.database)
        aut_dict = mgr.get_authors_dict(mgr.database)
        list_copy = list()
        for i in book_dict:
            if book_dict[i].book_is_active:
                list_copy.append(f"{book_dict[i].title} by {aut_dict[book_dict[i].author].fullname} ")
        list_copy.append('Exit')
        current_view = Menu("Book Database Menu", list_copy)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(list_copy) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            elif int(key) < len(book_list):
                temp_book_list = mgr.get_history_list_by_book(mgr.database, book_id_list[int(key)])
                usr_dict = mgr.get_users_dict(mgr.database)
                if not book_list:
                    logging.info(f"No history for {book_list[int(key)].title}, leaving.")
                    input()
                else:
                    user_list = [usr_dict[i].fullname for i in temp_book_list]
                    book_history_menu = Menu("Book History Menu", user_list)
                    book_history_menu.print_menu()
                    print("Press key to return")
                    input()
            else:
                logging.error('Wrong Key')
                break

    @staticmethod
    def prep_author_db(mgr: manager.LibraryManager):
        pass
        aut_list, aut_id_list = mgr.get_author_list(mgr.database)
        aut_list.append('Exit')
        current_view = Menu("Author Database Menu", aut_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(aut_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                logging.error('Wrong Key')

    @staticmethod
    def prep_borrow_menu(mgr: manager.LibraryManager):
        book_list, book_id_list = mgr.get_book_list(mgr.database)
        usr_list, usr_id_list = mgr.get_user_list(mgr.database)
        book_list.append('Exit')
        current_view = Menu("Borrow Menu", book_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(book_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                if not mgr.is_book_in_library(mgr.database, book_id_list[int(key)]):
                    logging.error("Book not available - press key to return")
                    input()
                    break

                user_menu = Menu("Choose user", usr_list)
                while 1:
                    user_menu.print_menu()
                    usr_key = input()
                    if int(usr_key) < len(usr_list):
                        usr_id = usr_id_list[int(usr_key)]
                        break
                    else:
                        logging.error("Wrong key! Try again!")
                mgr.borrow_a_book(mgr.database, book_id_list[int(key)], usr_id)
                logging.info("Press key to return")
                input()
                break

    @staticmethod
    def prep_return_menu(mgr: manager.LibraryManager):
        book_list, book_id_list = mgr.get_book_list(mgr.database)
        book_list.append('Exit')
        current_view = Menu("Return Menu", book_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(book_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                if mgr.is_book_in_library(mgr.database, book_id_list[int(key)]):
                    logging.error("Book in library, cannot return - press key to return")
                    input()
                    break
                mgr.return_a_book(mgr.database, book_id_list[int(key)])
                logging.info("Press key to return")
                input()
                break

    @staticmethod
    def add_book(mgr: manager.LibraryManager):
        pass
        aut_list, aut_id_list = mgr.get_author_list(mgr.database)
        cat_list, cat_id_list = mgr.get_category_list(mgr.database)
        title = input("Enter title\n")
        current_view = Menu("Choose author", aut_list)
        while 1:
            current_view.print_menu()
            key = input()
            if int(key) < len(aut_list):
                aut = aut_id_list[int(key)]
                break
            else:
                logging.error("Wrong key! Try again!")

        current_view = Menu("Choose category", cat_list)
        while 1:
            current_view.print_menu()
            key = input()
            if int(key) < len(cat_list):
                cat = cat_id_list[int(key)]
                break
            else:
                logging.error("Wrong key! Try again!")
        isbn = input("Enter isbn\n")
        try:
            mgr.database.add_book(title, aut, cat, isbn)
        except Error as err:
            logging.error(f"Error: {err.msg} !")
            return
        logging.info("Successfully added new book")
        input("Press key to continue\n")

    @staticmethod
    def add_author(mgr: manager.LibraryManager):
        aut_name = input("Enter authors name\n")
        aut_surname = input("Enter authors surname\n")
        try:
            mgr.database.add_author(aut_name, aut_surname)
        except Error as err:
            logging.error(f"Error: {err.msg} !")
            return
        logging.info("Successfully added new author")
        input("Press key to continue\n")

    @staticmethod
    def add_user(mgr: manager.LibraryManager):
        usr_name = input("Enter users name\n")
        usr_surname = input("Enter users surname\n")
        try:
            mgr.database.add_user(usr_name, usr_surname)
        except Error as err:
            logging.error(f"Error: {err.msg} !")
            return
        logging.info("Successfully added new user")
        input("Press key to continue\n")

    @staticmethod
    def add_book_cat(mgr: manager.LibraryManager):
        cat_name = input("Enter category name\n")
        try:
            mgr.database.add_category(cat_name)
        except Error as err:
            logging.error(f"Error: {err.msg} !")
            return
        logging.info("Successfully added new category")
        input("Press key to continue\n")

    @staticmethod
    def rem_book(mgr: manager.LibraryManager):
        book_list, book_id_list = mgr.get_book_list(mgr.database)
        book_list.append('Exit')
        current_view = Menu("Remove book", book_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(book_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                mgr.deactivate_book(mgr.database, book_id_list[int(key)])
                logging.info("Press key to return.")
                input()
                break

    @staticmethod
    def rem_author(mgr: manager.LibraryManager):
        aut_list, aut_id_list = mgr.get_author_list(mgr.database)
        aut_list.append('Exit')
        current_view = Menu("Remove author", aut_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(aut_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                mgr.deactivate_author(mgr.database, aut_id_list[int(key)])
                logging.info("Press key to return.")
                input()
                break

    @staticmethod
    def rem_user(mgr: manager.LibraryManager):
        usr_list, usr_id_list = mgr.get_user_list(mgr.database)
        usr_list.append('Exit')
        current_view = Menu("Remove user", usr_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(usr_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                mgr.deactivate_user(mgr.database, usr_id_list[int(key)])
                logging.info("Press key to return.")
                input()
                break

    @staticmethod
    def rem_book_cat(mgr: manager.LibraryManager):
        cat_list, cat_id_list = mgr.get_category_list(mgr.database)
        cat_list.append('Exit')
        current_view = Menu("Remove category", cat_list)
        while 1:
            current_view.print_menu()
            key = input()
            if key == str(len(cat_list) - 1) or key == '':
                logging.info("Leaving submenu")
                break
            else:
                mgr.deactivate_category(mgr.database, cat_id_list[int(key)])
                logging.info("Press key to return.")
                input()
                break


if __name__ == "__main__":
    test = MyApp()
