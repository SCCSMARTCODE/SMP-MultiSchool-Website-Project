from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class Login(FlaskForm):
    gmail = StringField("Gmail Address", validators=[DataRequired(), Email()])
    password = PasswordField("New password", validators=[DataRequired(), Length(min=7, max=19)])
    remember = BooleanField("remember me")
    submit = SubmitField("Login")
