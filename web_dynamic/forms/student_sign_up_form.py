from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from models.engine import storage

info = storage.all('School')
id_ = 1
list_of_schools = []
for key in info.keys():
    data = info[key].__dict__["name"]
    list_of_schools.append((id_, data))
    id_ += 1


class StudentRegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=4, max=40)])
    second_name = StringField("Second Name", validators=[DataRequired(), Length(min=4, max=40)])
    school = SelectField("Select School", choices=list_of_schools, validators=[DataRequired()])
    gmail = StringField("Gmail Address", validators=[DataRequired(), Email()])
    password = PasswordField("New password", validators=[DataRequired(), Length(min=7, max=19)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField("Sign up")
