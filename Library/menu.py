import manager as mg
import book_category as bc
import user as usr
import users_database as ub
import my_book as bk
import book_database as bb
import author as aut
import author_database as ab
import book_category_database as bcb

import curses

main_menu = ['Databases', 'Loan Book', 'Return Book', 'Add...', 'Remove...', 'Exit']
database_menu = ['User database', 'Book database', 'Book category database', 'Author database', 'Exit']
action_menu = ['Book', 'Author', 'User', 'Category', 'Exit']


def print_list(stdscr, selected_row_idx, menu_type: list, title: str = ""):
    stdscr.clear()
    h, w, = stdscr.getmaxyx()
    x = w // 2 - len(title) // 2
    y = 0
    stdscr.addstr(y, x, title)
    for idx, row in enumerate(menu_type):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu_type) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


'''###########################################################'''
'''##################  DATABASE  #############################'''
'''###########################################################'''


def pop_database_menu(stdscr, current_row, mgr: mg.LibraryManager):
    while 1:
        print_list(stdscr, current_row, database_menu)
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(database_menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(database_menu) - 1:
                break
            elif str(database_menu[current_row]) == 'User database':
                pop_user_db(stdscr, mgr)
            elif str(database_menu[current_row]) == 'Book category database':
                pop_book_cat_db(stdscr, mgr)
            elif str(database_menu[current_row]) == 'Book database':
                pop_book_db(stdscr, mgr)
            elif str(database_menu[current_row]) == 'Author database':
                pop_aut_db(stdscr, mgr)


def pop_user_db(stdscr, mgr: mg.LibraryManager):
    current_row = 0
    list_copy = mgr.user_database.return_list()
    list_copy.append('Exit')
    while 1:
        print_list(stdscr, current_row, list_copy, "Users")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break
            else:
                history_list = list()
                usr_id = mgr.user_database.get_id(list_copy[current_row])
                for i in mgr.history['User'][usr_id]:
                    history_list.append(mgr.book_database.book_dict[i].title)
                if len(history_list) == 0:
                    print_list(stdscr, 0, ['Empty'], f'History of "{list_copy[current_row]}"')
                    stdscr.getch()
                else:
                    print_list(stdscr, current_row, history_list, f'History of "{list_copy[current_row]}"')
                    stdscr.getch()


def pop_book_cat_db(stdscr, mgr: mg.LibraryManager):
    current_row = 0
    list_copy = mgr.book_category_database.return_list()
    list_copy.append('Exit')
    while 1:
        print_list(stdscr, current_row, list_copy, "Book Categories")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break
            else:
                by_cat = mgr.list_by_category()
                if str(current_row) not in by_cat.keys():
                    print_list(stdscr, 0, ['Empty'], "Book Categories")
                    stdscr.getch()
                else:
                    print_list(stdscr, 0, by_cat[str(current_row)], "Book Categories")
                    stdscr.getch()


def pop_book_db(stdscr, mgr: mg.LibraryManager):
    current_row = 0
    book_dict, id_list = mgr.book_database.return_dict_by_author()
    aut_list = mgr.author_database.return_list()
    usr_list = mgr.user_database.return_list()
    list_copy = list()
    for i in book_dict:
        list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
    list_copy.append('Exit')
    while 1:
        print_list(stdscr, current_row, list_copy, "Books")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break
            else:
                history_list = list()
                book_id = id_list[current_row]
                for i in mgr.history['Book'][book_id]:
                    history_list.append(usr_list[int(i)])
                print_list(stdscr, current_row, history_list, f'History of "{mgr.book_database.book_dict[book_id].title}"')
                stdscr.getch()



def pop_aut_db(stdscr, mgr: mg.LibraryManager):
    current_row = 0
    list_copy = mgr.author_database.return_list()
    list_copy.append('Exit')
    while 1:
        print_list(stdscr, current_row, list_copy, "Authors")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break


'''###########################################################'''
'''################  DATABASE END  ###########################'''
'''###########################################################'''

'''###########################################################'''
'''##################  ADD MENU  #############################'''
'''###########################################################'''


def pop_add_menu(stdscr, current_row, mgr: mg.LibraryManager):
    while 1:
        print_list(stdscr, current_row, action_menu, "Add:")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(action_menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(action_menu) - 1:
                break
            elif str(action_menu[current_row]) == 'Book':
                add_book(stdscr, mgr.book_database)
            elif str(action_menu[current_row]) == 'Author':
                add_author(stdscr, mgr.author_database)
            elif str(action_menu[current_row]) == 'User':
                add_user(stdscr, mgr.user_database)
            elif str(action_menu[current_row]) == 'Category':
                add_category(stdscr, mgr.book_category_database)


def add_book(stdscr, bdb: bb.BookDataBase):
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Title") // 2, "Title")
    title = read_word(stdscr, h, w)
    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Isbn") // 2, "Isbn")
    isbn = read_word(stdscr, h, w)
    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Category") // 2, "Category")
    category = read_word(stdscr, h, w)
    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Author id") // 2, "Author id")
    aut_id = read_word(stdscr, h, w)
    book = bk.MyBook(aut_id, title, isbn, category)
    if bdb.add_book(book):
        bdb.save_books()
        print_center(stdscr, "Success - press key to return")
        stdscr.getch()
    else:
        print_center(stdscr, "Error - press key to return")
        stdscr.getch()


def add_author(stdscr, adb: ab.AuthorDataBase):
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Name") // 2, "Name")
    name = read_word(stdscr, h, w)
    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Surname") // 2, "Surname")
    surname = read_word(stdscr, h, w)
    aut_id = int(adb.get_max_id()) + 1
    au = aut.Author(str(aut_id), name, surname)
    if adb.add_author(au):
        adb.save_author()
        print_center(stdscr, "Success - press key to return")
        stdscr.getch()
    else:
        print_center(stdscr, "Error - press key to return")
        stdscr.getch()


def add_user(stdscr, udb: ub.UserDataBase):
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Name") // 2, "Name")
    name = read_word(stdscr, h, w)
    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Surname") // 2, "Surname")
    surname = read_word(stdscr, h, w)
    usr_id = int(udb.get_max_id()) + 1

    us = usr.User(str(usr_id), name, surname)
    if udb.add_user(us):
        udb.save_users()
        print_center(stdscr, "Success - press key to return")
        stdscr.getch()
    else:
        print_center(stdscr, "Error - press key to return")
        stdscr.getch()


def add_category(stdscr, cat: bcb.BookCategoryDataBase):
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.addstr(0, w // 2 - len("Category name") // 2, "Category name")
    name = read_word(stdscr, h, w)
    cat_id = int(cat.get_max_id()) + 1
    bcat = bc.BookCategory(name, str(cat_id))
    if cat.add_book_cat(bcat):
        cat.save_book_cat()
        print_center(stdscr, "Success - press key to return")
        stdscr.getch()
    else:
        print_center(stdscr, "Error - press key to return")
        stdscr.getch()


def read_word(stdscr, h, w):
    word = str()
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            break
        word += chr(key)
        x = w // 2 - len(word) // 2
        y = h // 2
        stdscr.addstr(y, x, word)
        stdscr.refresh()
    return word


'''###########################################################'''
'''################  ADD MENU END  ###########################'''
'''###########################################################'''

'''###########################################################'''
'''#################  REMOVE MENU  ###########################'''
'''###########################################################'''


def pop_remove_menu(stdscr, current_row, mgr: mg.LibraryManager):
    while 1:
        print_list(stdscr, current_row, action_menu, "Remove:")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(action_menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(action_menu) - 1:
                break
            elif str(action_menu[current_row]) == 'Book':
                rem_book(stdscr, mgr.book_database, mgr.author_database)
            elif str(action_menu[current_row]) == 'Author':
                rem_author(stdscr, mgr.author_database)
            elif str(action_menu[current_row]) == 'User':
                rem_user(stdscr, mgr.user_database)
            elif str(action_menu[current_row]) == 'Category':
                rem_category(stdscr, mgr.book_category_database)


def rem_author(stdscr, adb: ab.AuthorDataBase):
    current_row = 0
    temp_list = adb.return_list()
    temp_list.append('Exit')
    while 1:
        print_list(stdscr, current_row, temp_list, "Authors")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(temp_list) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(temp_list) - 1:
                break
            else:
                rem_id = adb.get_id(temp_list[current_row])
                if adb.remove_author(rem_id):
                    adb.save_author()
                    print_center(stdscr, "Success - press key to return")
                    stdscr.getch()
                else:
                    print_center(stdscr, "Error - press key to return")
                    stdscr.getch()
                break


def rem_book(stdscr, bdb: bb.BookDataBase, adb: ab.AuthorDataBase):
    current_row = 0
    book_dict, id_list = bdb.return_dict_by_author()
    aut_list = adb.return_list()
    list_copy = list()
    for i in book_dict:
        list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
    list_copy.append('Exit')

    while 1:
        print_list(stdscr, current_row, list_copy, "Books")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break
            else:
                if bdb.remove_book(id_list[current_row]):
                    bdb.save_books()
                    print_center(stdscr, "Success - press key to return")
                    stdscr.getch()
                else:
                    print_center(stdscr, "Error - press key to return")
                    stdscr.getch()
                break


def rem_category(stdscr, cat: bcb.BookCategoryDataBase):
    current_row = 0
    temp_list = cat.return_list()
    temp_list.append('Exit')
    while 1:
        print_list(stdscr, current_row, temp_list, "Book Categories")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(temp_list) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(temp_list) - 1:
                break
            else:
                rem_id = cat.get_id(temp_list[current_row])
                if cat.remove_book_cat(rem_id):
                    cat.save_book_cat()
                    print_center(stdscr, "Success - press key to return")
                    stdscr.getch()
                else:
                    print_center(stdscr, "Error - press key to return")
                    stdscr.getch()
                break


def rem_user(stdscr, udb: ub.UserDataBase):
    current_row = 0
    temp_list = udb.return_list()
    temp_list.append('Exit')
    while 1:
        print_list(stdscr, current_row, temp_list, "Users")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(temp_list) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(temp_list) - 1:
                break
            else:
                rem_id = udb.get_id(temp_list[current_row])
                if rem_id == "0":
                    print_center(stdscr, "Error! Cannot remove library - press key to return")
                    stdscr.getch()
                    break
                if udb.remove_user(rem_id):
                    udb.save_users()
                    print_center(stdscr, "Success - press key to return")
                    stdscr.getch()
                else:
                    print_center(stdscr, "Error - press key to return")
                    stdscr.getch()
                break


'''###########################################################'''
'''###############  REMOVE MENU END  #########################'''
'''###########################################################'''

'''###########################################################'''
'''#################  LOAN BOOK MENU  ########################'''
'''###########################################################'''


def pop_loan_book(stdscr, mgr: mg.LibraryManager):
    current_row = 0
    book_dict, id_list = mgr.book_database.return_dict_by_author()
    aut_list = mgr.author_database.return_list()
    list_copy = list()
    for i in book_dict:
        list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
    list_copy.append('Exit')
    while 1:
        print_list(stdscr, current_row, list_copy, "Loan Book")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break
            else:
                if not mgr.book_database.is_book_available(id_list[current_row]):
                    print_center(stdscr, "Book not available - press key to return")
                    stdscr.getch()
                    break

                h, w = stdscr.getmaxyx()
                stdscr.clear()
                stdscr.addstr(0, w // 2 - len("Enter Users ID") // 2, "Enter Users ID")
                user_id = read_word(stdscr, h, w)
                if mgr.loan_a_book(id_list[current_row], str(user_id)):
                    print_center(stdscr, "Success - press key to return")
                    stdscr.getch()
                else:
                    print_center(stdscr, "Error - press key to return")
                    stdscr.getch()
                break


'''###########################################################'''
'''#################  LOAN BOOK MENU  ########################'''
'''###########################################################'''

'''###########################################################'''
'''#################  LOAN BOOK MENU  ########################'''
'''###########################################################'''


def pop_return_book(stdscr, mgr: mg.LibraryManager):
    current_row = 0
    book_dict, id_list = mgr.book_database.return_dict_by_author()
    aut_list = mgr.author_database.return_list()
    list_copy = list()
    for i in book_dict:
        list_copy.append(f"{book_dict[i]} by {aut_list[int(i)]} ")
    list_copy.append('Exit')
    while 1:
        print_list(stdscr, current_row, list_copy, "Loan Book")
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(list_copy) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(list_copy) - 1:
                break
            else:
                if mgr.return_a_book(id_list[current_row]):
                    print_center(stdscr, "Success - press key to return")
                    stdscr.getch()
                else:
                    print_center(stdscr, "Error - press key to return")
                    stdscr.getch()
                break


'''###########################################################'''
'''#################  LOAN BOOK MENU  ########################'''
'''###########################################################'''


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main_disp(stdscr):
    manager = mg.LibraryManager()
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_list(stdscr, current_row, main_menu)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(main_menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if str(main_menu[current_row]) == 'Databases':
                pop_database_menu(stdscr, current_row, manager)
                current_row = 0
            elif str(main_menu[current_row]) == 'Add...':
                pop_add_menu(stdscr, 0, manager)
                current_row = 0
            elif str(main_menu[current_row]) == 'Loan Book':
                pop_loan_book(stdscr, manager)
            elif str(main_menu[current_row]) == 'Return Book':
                pop_return_book(stdscr, manager)
            elif str(main_menu[current_row]) == 'Remove...':
                pop_remove_menu(stdscr, 0, manager)
                current_row = 0
            else:
                # if user selected last row, exit the program
                if current_row == len(main_menu) - 1:
                    break
                print_center(stdscr, "You selected '{}'".format(main_menu[current_row]))
                stdscr.getch()

        print_list(stdscr, current_row, main_menu)


def test():
    curses.wrapper(main_disp)
