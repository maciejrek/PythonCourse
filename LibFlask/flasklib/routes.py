from flask import render_template, flash, url_for, redirect, request, abort
from flasklib.forms import AddUserForm, AddAuthorForm, AddCategoryForm, AddBookForm, RemoveDatabase
from flasklib import app
from flasklib import manager

mgr = manager.LibraryManager()


@app.route("/")
def mainpage():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template('home.html', title='Main page')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/user_db", methods=['GET', 'POST'])
def user_db():
    """ Not sure if this is the way to do this, but without commit i couldn't refresh data from sql server on webapp """
    form = AddUserForm(request.form)
    if form.validate_on_submit():
        mgr.database.add_user(form.name.data, form.surname.data)
        flash(f"User {form.name.data} {form.surname.data} created!", 'success')
        return redirect(url_for('user_db'))
    return render_template('user_db.html', title='User database', posts=mgr.prep_user(mgr.database), form=form)


@app.route("/deactivate/<who>/<uid>", methods=['POST'])
def deactivate_something(who=None, uid=None):
    print(who, uid)
    if who == 'user':
        mgr.deactivate_user(mgr.database, uid)
        return redirect(url_for('user_db'))
    elif who == "author":
        mgr.deactivate_author(mgr.database, uid)
        return redirect(url_for('author_db'))
    elif who == "category":
        mgr.deactivate_category(mgr.database, uid)
        return redirect(url_for('category_db'))
    elif who == "book":
        mgr.deactivate_book(mgr.database, uid)
        return redirect(url_for('book_db'))
    return redirect(url_for('home'))


@app.route("/activate/<who>/<uid>", methods=['POST'])
def activate_something(who=None, uid=None):
    if who == 'user':
        mgr.activate_user(mgr.database, uid)
        return redirect(url_for('user_db'))
    elif who == "author":
        mgr.activate_author(mgr.database, uid)
        return redirect(url_for('author_db'))
    elif who == "category":
        mgr.activate_category(mgr.database, uid)
        return redirect(url_for('category_db'))
    elif who == "book":
        mgr.activate_book(mgr.database, uid)
        return redirect(url_for('book_db'))
    return redirect(url_for('home'))


@app.route("/book_db", methods=['GET', 'POST'])
def book_db():
    form = AddBookForm(request.form)
    form.category.choices = mgr.get_category_tuple_list(mgr.database)
    form.author.choices = mgr.get_author_tuple_list(mgr.database)
    if form.validate_on_submit():
        mgr.database.add_book(form.title.data, form.author.data, form.category.data, form.isbn.data)
        flash(f"Book {form.title.data} created!", 'success')
        return redirect(url_for('book_db'))
    return render_template('book_db.html', title='Book database', posts=mgr.prep_book(mgr.database), form=form)


@app.route("/borrow_a_book/<book_uid>/<usr_uid>", methods=['GET', 'POST'])
def borrow_a_book(book_uid=None, usr_uid=None):
    if usr_uid == '-1':
        if mgr.is_book_in_library(mgr.database, book_uid):
            return render_template('borrow_book.html', title='User database',
                                   posts={'usr_db': mgr.prep_user(mgr.database), 'book_uid': book_uid})
        else:
            flash(f"Cannot borrow book - already borrowed!", 'danger')
    else:
        if mgr.is_book_in_library(mgr.database, book_uid):
            mgr.borrow_a_book(mgr.database, book_uid, usr_uid)
            flash(f"Borrowed a book!", 'success')
            return redirect(url_for('borrows'))
        else:
            flash(f"Failed to borrow a book!", 'danger')
    return redirect(url_for('home'))


@app.route("/return_book/<uid>", methods=['GET', 'POST'])
def return_a_book(uid=None):
    if not mgr.is_book_in_library(mgr.database, uid):
        mgr.return_a_book(mgr.database, uid)
        flash(f"Returned a book!", 'success')
    else:
        flash(f"Failed to return a book!", 'danger')
    return redirect(url_for('borrows'))


@app.route("/author_db", methods=['GET', 'POST'])
def author_db():
    form = AddAuthorForm(request.form)
    if form.validate_on_submit():
        mgr.database.add_author(form.name.data, form.surname.data)
        flash(f"Author {form.name.data} {form.surname.data} created!", 'success')
        return redirect(url_for('author_db'))
    return render_template('author_db.html', title='Author database', posts=mgr.prep_author(mgr.database), form=form)


@app.route("/category_db", methods=['GET', 'POST'])
def category_db():
    form = AddCategoryForm(request.form)
    if form.validate_on_submit():
        mgr.database.add_category(form.name.data)
        flash(f"Category {form.name.data} created!", 'success')
        return redirect(url_for('category_db'))
    return render_template('category_db.html', title='Category database', posts=mgr.prep_category(mgr.database),
                           form=form)


@app.route("/inactives", methods=['GET', 'POST'])
def inactives():
    return render_template('inactives.html', title='Inactive positions', posts=mgr.database.return_inactive())


@app.route("/borrows", methods=['GET', 'POST'])
def borrows():
    return render_template('borrows.html', title='History of borrows', posts=mgr.prep_history(mgr.database))


@app.route("/remove", methods=['GET', 'POST'])
def remove_database():
    form = RemoveDatabase(request.form)
    if form.validate_on_submit() and form.decision.data == "YES":
        mgr.database.remove_db("LibraryDatabase")
        mgr.database.prepare_db("LibraryDatabase")
        return redirect(url_for('home'))
    return render_template('removedb.html', form=form)
