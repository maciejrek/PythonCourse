from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp


class AddUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),
                                           Regexp(regex=r'[A-Z,a-z]\w+',
                                                  message="User name must contain only letters."),
                                           Length(min=1, max=20)])
    surname = StringField('Surname',
                          validators=[DataRequired(),
                                      Regexp(regex=r'[A-Z,a-z]\w+', message="User surname must contain only letters."),
                                      Length(min=1, max=20)])
    submit = SubmitField('Add User')


class AddAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),
                                           Regexp(regex=r'[A-Z,a-z]\w+',
                                                  message="Author name must contain only letters."),
                                           Length(min=1, max=20)])
    surname = StringField('Surname', validators=[DataRequired(),
                                                 Regexp(regex=r'[A-Z,a-z]\w+',
                                                        message="Author surname must contain only letters."),
                                                 Length(min=1, max=20)])
    submit = SubmitField('Add Author')


class AddCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),
                                           Regexp(regex=r'[A-Z,a-z]\w+',
                                                  message="Category name must contain only letters."),
                                           Length(min=1, max=20)])
    submit = SubmitField('Add Category')


class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),
                                             Regexp(regex=r'[A-Z a-z.!?-]\w+',
                                                    message="Title must contain only [A-Z a-z .!?-]."),
                                             Length(min=1, max=50)])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    author = SelectField('Author', coerce=int, validators=[DataRequired()])
    isbn = IntegerField('ISBN', validators=[DataRequired(), NumberRange(min=100000, max=999999)])
    submit = SubmitField('Add Book')


class RemoveDatabase(FlaskForm):
    decision = StringField('Type "YES" to remove database', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Submit')
