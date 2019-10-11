import manager

test = manager.LibraryManager()


a = test.get_users_dict(test.database)
for i in a:
    print(a[i].usr_is_active)

print(a)

a = test.get_authors_dict(test.database)
for i in a:
    print(a[i].aut_is_active)

print(a)

a = test.get_category_dict(test.database)
for i in a:
    print(a[i].cat_is_active)

print(a)

a = test.get_book_dict(test.database)
for i in a:
    print(a[i].book_is_active)

print(a)


#
# # logging.basicConfig(level=logging.INFO)
# # a = menu_module.MyApp()
#
# lib = LibDb.prepare_database("LibraryDatabase")
# lib.show_db()
#
# lib.show_columns("user")
# lib.show_columns("book")
# lib.show_columns("author")
# lib.show_columns("category")
# lib.show_columns("history")
#
# # lib.add_author("Andrzej", "Kowalski")
# # lib.add_author("Jan", "Stanislaw")
# # lib.add_category("Horror")
# # lib.add_category("Romance")
# # lib.add_book("Skazani na pasztet", 1, 2, 173295)
# # lib.add_book("Bez pradu", 2, 1, 913235)
# # lib.add_user("Jan", "Staranny")
# # lib.add_user("Stefan", "Kolano")
#
print("######################################")
test.database.execute("SELECT * FROM book")
x = test.database.response()
print("print book:\n", x)

test.database.execute("SELECT * FROM user")
x = test.database.response()
print("print user:\n", x)

test.database.execute("SELECT * FROM author")
x = test.database.response()
print("print author:\n", x)

test.database.execute("SELECT * FROM category")
x = test.database.response()
print("print category:\n", x)

test.database.execute("SELECT * FROM history")
x = test.database.response()
print("print history:\n", x)

print("######################################")
test.database.execute("SELECT * FROM book WHERE active = 0")
x = test.database.response()
print("print book:\n", x)

test.database.execute("SELECT * FROM user WHERE active = 0")
x = test.database.response()
print("print user:\n", x)

test.database.execute("SELECT * FROM author WHERE active = 0")
x = test.database.response()
print("print author:\n", x)

test.database.execute("SELECT * FROM category WHERE active = 0")
x = test.database.response()
print("print category:\n", x)

test.database.set_active("book",1)
test.database.set_active("book",2)
test.database.set_active("book",3)
test.database.set_active("book",4)
test.database.set_active("user",3)
test.database.set_active("author",2)
test.database.set_active("category",4)


# print(lib.return_tab_by_param("name, surname", "user"))
# print(lib.return_tab_by_param("name, surname", "author"))
# print(lib.return_tab_by_param("name", "category"))
# print(lib.return_tab_by_param("id_category", "book"))
# # lib.remove_db("LibraryDatabase")
#
#
#
#


# CONNECT DO DB {NAME}
# name = "TestDb"
# lib = LibDb("localhost", "root", "root")
# lib.show_db()
# while 1:
#     try:
#         lib.execute(f"USE {name}")
#         logging.info("Connected")
#         break
#     except Error as err:
#         if err.errno == mc.errorcode.ER_BAD_DB_ERROR:
#             logging.error(f"{err.msg}!")
#             lib.prepare_db(name)
#             sleep(1)
#             break
#         else:
#             logging.error(f"ERROR {err.msg}!")
#             sleep(1)
#
# lib.show_columns("history")
# lib.execute("SELECT * FROM user")
# lib.add_author("First", "Author")
# lib.add_category("Name")
# lib.add_book("title", 1, 1, 123123)
# lib.add_user("First", "User")
# lib.execute("SELECT * FROM book")
# x = lib.response()
# print("print book:\n", x)
# print("Borrow\n")
# lib.borrow_a_book(1, 1)
# lib.execute("SELECT * FROM history")
# x = lib.response()
# print("print History:\n", x)
# lib.execute("SELECT * FROM book")
# x = lib.response()
# print("print book:\n", x)
# print("return\n")
# lib.return_a_book(1)
# lib.execute("SELECT * FROM history")
# x = lib.response()
# print("print history:\n", x)
# lib.execute("SELECT * FROM book")
# x = lib.response()
# print("print book:\n", x)
# lib.remove_db("TestDb")
