from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class AddUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Add User')


class AddAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Add Author')


class AddCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Add Category')


class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=50)])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    author = SelectField('Author', coerce=int, validators=[DataRequired()])
    isbn = IntegerField('ISBN', validators=[DataRequired(), NumberRange(min=100000, max=999999)])
    submit = SubmitField('Add Book')


class RemoveDatabase(FlaskForm):
    decision = StringField('Type "YES" to remove database', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Submit')
