from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields import TelField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SchoolRegistrationForm(FlaskForm):
    name = StringField("School Name", validators=[DataRequired(), Length(min=4, max=40)])
    address = StringField("School Address", validators=[DataRequired(), Length(min=30, max=290)])
    gmail = StringField("School Gmail Address", validators=[DataRequired(), Email()])
    phone_address = TelField("School Phone Address", validators=[DataRequired()])
    password = PasswordField("New password", validators=[DataRequired(), Length(min=7, max=19)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField("Sign up")


