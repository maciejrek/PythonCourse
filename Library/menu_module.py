import manager
import logging
import my_book
import author
import user
import book_category


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


class SubMenu(Menu):

    def __init__(self, name, lista):
        Menu.__init__(self, name, lista)


def prep_book_list(mgr: manager.LibraryManager):
    book_dict, id_list = mgr.book_database.return_dict_by_author()
    aut_list = mgr.author_database.return_list()
    list_copy = list()
    for i in book_dict:
        list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
    list_copy.append('Exit')
    return list_copy


class MyApp:
    main_menu_l = ['Databases', 'Loan Book', 'Return Book', 'Add...', 'Remove...', 'Exit']
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
                self.prep_loan_menu(mgr)
            elif key == "2":
                self.prep_return_menu(mgr)
            elif key == "3":
                self.prep_add_menu(mgr)
            elif key == "4":
                self.prep_remove_menu(mgr)
            else:
                print("Finishing program")
                break

    # DATABASE FUNCTIONALITY
    def prep_database_menu(self, mgr: manager.LibraryManager):
        self.db_submenu = SubMenu("Database Menu", MyApp.db_submenu_l)
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
        self.add_menu = SubMenu("Add:", MyApp.action_menu_l)
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
        self.remove_menu = SubMenu("Remove:", MyApp.action_menu_l)
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
    def prep_user_db(mgr: manager.LibraryManager):
        list_copy = mgr.user_database.return_list()
        list_copy.append('Exit')
        user_db_menu = SubMenu("User Database Menu", list_copy)
        while 1:
            user_db_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            elif key == "0":
                logging.error("There's no history stored for user 'Library'\nPress key to return")
                input()
                break

            elif int(key) < len(list_copy):
                history_list = list()
                usr_id = mgr.user_database.get_id(list_copy[int(key)])
                for i in mgr.history['User'][usr_id]:
                    history_list.append(mgr.book_database.book_dict[i].title)
                user_history_menu = SubMenu("User History Menu", history_list)
                user_history_menu.print_menu()
                print("Press key to return")
                input()
                break
            else:
                logging.error("Wrong key!")

    @staticmethod
    def prep_book_cat_db(mgr: manager.LibraryManager):
        list_copy = mgr.book_category_database.return_list()
        list_copy.append('Exit')
        book_cat_menu = SubMenu("Book Category Database Menu", list_copy)
        while 1:
            book_cat_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                by_cat = mgr.list_by_category()
                if key not in by_cat.keys() and int(key) < len(list_copy):
                    logging.info('Empty!')
                    input()
                elif int(key) < len(list_copy):
                    book_cat_list = SubMenu("Book Category List", by_cat[key])
                    book_cat_list.print_menu()
                    input()
                    break
                else:
                    logging.error('Wrong Key')

    @staticmethod
    def prep_book_db(mgr: manager.LibraryManager):
        book_dict, id_list = mgr.book_database.return_dict_by_author()
        aut_list = mgr.author_database.return_list()
        usr_list = mgr.user_database.return_list()
        list_copy = list()
        for i in book_dict:
            list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
        list_copy.append('Exit')
        book_menu = SubMenu("Book Database Menu", list_copy)
        while 1:
            book_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                history_list = list()
                book_id = id_list[int(key)]
                for i in mgr.history['Book'][book_id]:
                    history_list.append(usr_list[int(i)])
                book_history_menu = SubMenu("Book History Menu", history_list)
                book_history_menu.print_menu()
                print("Press key to return")
                input()
                break

    @staticmethod
    def prep_author_db(mgr: manager.LibraryManager):
        list_copy = mgr.author_database.return_list()
        list_copy.append('Exit')
        aut_menu = SubMenu("Author Database Menu", list_copy)
        while 1:
            aut_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                logging.error('Wrong Key')

    @staticmethod
    def prep_loan_menu(mgr: manager.LibraryManager):
        loan_submenu = SubMenu("Loan Menu", prep_book_list(mgr))
        id_list = mgr.book_database.return_dict_by_author()
        while 1:
            loan_submenu.print_menu()
            key = input()
            if key == str(len(MyApp.db_submenu_l) - 1):
                logging.info("Leaving submenu")
                break
            else:
                if not mgr.book_database.is_book_available(id_list[1][int(key)]):
                    logging.error("Book not available - press key to return")
                    input()
                    break
                logging.info("Enter Users ID")
                user_id = input()
                if mgr.loan_a_book(id_list[1][int(key)], user_id):
                    logging.info("Success - press key to return")
                    input()
                    break
                else:
                    logging.error("Error - press key to return")
                    input()
                    break

    @staticmethod
    def prep_return_menu(mgr: manager.LibraryManager):
        list_copy = prep_book_list(mgr)
        id_list = mgr.book_database.return_dict_by_author()
        return_submenu = SubMenu("Return Menu", list_copy)
        while 1:
            return_submenu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            elif int(key) < len(list_copy):
                if mgr.return_a_book(id_list[1][int(key)]):
                    logging.info("Success - press key to return")
                    input()
                    break
                else:
                    logging.error("Error - press key to return")
                    input()
                    break
            else:
                logging.error("Key not available - leaving submenu")
                break

    def add_book(self, mgr: manager.LibraryManager):
        title = input("Enter title\n")
        aut_id = input("Enter author id\n")
        category = input("Enter category\n")
        isbn = input("Enter isbn\n")
        if not self.verify_book_params(mgr, aut_id, isbn, category):
            logging.error("Cannot prepare book - wrong input parameters")
            return False
        book = my_book.MyBook(aut_id, title, isbn, category)
        if mgr.book_database.add_book(book):
            mgr.book_database.save_books()
            logging.info("Success - press key to return")
            input()
        else:
            logging.info("Error - press key to return")
            input()

    @staticmethod
    def add_author(mgr: manager.LibraryManager):
        aut_name = input("Enter authors name\n")
        aut_surname = input("Enter authors surname\n")
        aut_id = int(mgr.author_database.get_max_id()) + 1
        au = author.Author(str(aut_id), aut_name, aut_surname)
        if mgr.author_database.add_author(au):
            mgr.author_database.save_author()
            logging.info("Success - press key to return")
            input()
        else:
            logging.info("Error - press key to return")
            input()

    @staticmethod
    def add_user(mgr: manager.LibraryManager):
        usr_name = input("Enter users name\n")
        usr_surname = input("Enter users surname\n")
        usr_id = int(mgr.user_database.get_max_id()) + 1
        usr = user.User(str(usr_id), usr_name, usr_surname)
        if mgr.user_database.add_user(usr):
            mgr.user_database.save_users()
            logging.info("Success - press key to return")
            input()
        else:
            logging.info("Error - press key to return")
            input()

    @staticmethod
    def add_book_cat(mgr: manager.LibraryManager):
        cat_name = input("Enter category name\n")
        cat_id = int(mgr.book_category_database.get_max_id()) + 1
        bc = book_category.BookCategory(cat_name, str(cat_id))
        if mgr.book_category_database.add_book_cat(bc):
            mgr.book_category_database.save_book_cat()
            logging.info("Success - press key to return")
            input()
        else:
            logging.info("Error - press key to return")
            input()

    @staticmethod
    def verify_book_params(mgr: manager.LibraryManager, aut_id: str, isbn: str, category: str):
        if not mgr.author_database.is_author_in_db(aut_id):
            return False
        if mgr.book_database.is_book_in_db(isbn):
            return False
        if not mgr.book_category_database.is_book_cat_in_db(category):
            return False
        return True

    @staticmethod
    def rem_book(mgr: manager.LibraryManager):
        book_dict, id_list = mgr.book_database.return_dict_by_author()
        aut_list = mgr.author_database.return_list()
        list_copy = list()
        for i in book_dict:
            list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
        list_copy.append('Exit')
        remove_book_menu = SubMenu("Remove book", list_copy)
        while 1:
            remove_book_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                if mgr.book_database.remove_book(id_list[int(key)]):
                    mgr.book_database.save_directory
                    logging.info("Success - press key to return")
                    input()
                else:
                    logging.info("Error - press key to return")
                    input()
            break

    @staticmethod
    def rem_author(mgr: manager.LibraryManager):
        list_copy = mgr.author_database.return_list()
        list_copy.append('Exit')
        remove_aut_menu = SubMenu("Remove author:", list_copy)
        while 1:
            remove_aut_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                rem_id = mgr.author_database.get_id(list_copy[int(key)])
                if mgr.author_database.remove_author(rem_id):
                    mgr.author_database.save_author()
                    logging.info("Success - press key to return")
                    input()
                else:
                    logging.info("Error - press key to return")
                    input()
            break

    @staticmethod
    def rem_user(mgr: manager.LibraryManager):
        list_copy = mgr.user_database.return_list()
        list_copy.append('Exit')
        remove_usr_menu = SubMenu("Remove user:", list_copy)
        while 1:
            remove_usr_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                rem_id = mgr.user_database.get_id(list_copy[int(key)])
                if mgr.user_database.remove_user(rem_id):
                    mgr.user_database.save_users()
                    logging.info("Success - press key to return")
                    input()
                else:
                    logging.info("Error - press key to return")
                    input()
            break

    @staticmethod
    def rem_book_cat(mgr: manager.LibraryManager):
        list_copy = mgr.book_category_database.return_list()
        list_copy.append('Exit')
        remove_book_cat_menu = SubMenu("Remove book category:", list_copy)
        while 1:
            remove_book_cat_menu.print_menu()
            key = input()
            if key == str(len(list_copy) - 1):
                logging.info("Leaving submenu")
                break
            else:
                rem_id = mgr.book_category_database.get_id(list_copy[int(key)])
                if rem_id == "0":
                    logging.error("Error! Cannot remove library - press key to return")
                    break
                if mgr.book_category_database.remove_book_cat(rem_id):
                    mgr.book_category_database.save_book_cat()
                    logging.info("Success - press key to return")
                    input()
                else:
                    logging.info("Error - press key to return")
                    input()
            break
