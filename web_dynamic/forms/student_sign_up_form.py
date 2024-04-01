from os import environ


"""This should be removed ASAP"""
environ["DB_PASSWD"] = "smp_pass_master"
environ["DB_HOST"] = "localhost"
environ["DB_USER"] = "smp_master"
environ["DB_NAME"] = "smp_base_db"
environ["DB_TYPE"] = "db"
"""This should be removed ASAP"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_bcrypt import Bcrypt
from models.engine import storage
from models.engine import storage
from models.student import Student


bcrypt = Bcrypt()

def get_class(val):
    info = storage.all('School')
    id_ = 1
    list_of_schools = []
    id_with_school = []
    for key in info.keys():
        if info[key].__dict__["role"] != 'SMP_ADMIN':
            data = info[key].__dict__["name"]
            list_of_schools.append((id_, data))
            id_with_school.append([info[key].__dict__["id"], info[key].__dict__["name"]])
            id_ += 1
    if val == 0:
        return list_of_schools
    elif val == 1:
        return id_with_school


class StudentRegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=40)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=40)])
    school = SelectField("Select School", coerce=int, validators=[DataRequired()])
    gmail = StringField("Gmail Address", validators=[DataRequired(), Email()])
    password = PasswordField("New password", validators=[DataRequired(), Length(min=7, max=15)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password'),  Length(min=7, max=15)])
    submit = SubmitField("Sign up")

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.school.choices = get_class(0)

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        # Check if email already exists
        if self.gmail.data.lower() in (student.gmail for student in storage.all('Student').values()):
            self.gmail.errors.append("Email address already registered.")
            return False

        passwords_ = list([student.password for student in storage.all('Student').values()])
        for password_ in passwords_:
            if bcrypt.check_password_hash(password_, self.password.data):
                self.password.errors.append("Password already used.")
                return False

        return True

