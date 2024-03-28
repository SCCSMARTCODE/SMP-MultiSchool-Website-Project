from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.fields import TelField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_bcrypt import Bcrypt
from flask_login import current_user

bcrypt = Bcrypt()


class SchoolRegistrationForm(FlaskForm):
    name = StringField("School Name", validators=[DataRequired(), Length(min=4, max=40)])
    address = StringField("School Address", validators=[DataRequired(), Length(min=30, max=290)])
    gmail = StringField("School Gmail Address", validators=[DataRequired(), Email()])
    phone_address = TelField("School Phone Address", validators=[DataRequired()])
    password = PasswordField("New password", validators=[DataRequired(), Length(min=7, max=19)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password'), Length(min=7, max=19)])
    submit = SubmitField("Sign up")

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        from models.engine import storage
        # Check if email already exists
        if self.gmail.data.lower() in (school.gmail for school in storage.all('School').values()):
            self.gmail.errors.append("Email address already registered.")
            return False

        # Check if name already exists
        if self.name.data.title() in (school.name for school in storage.all('School').values()):
            self.name.errors.append("School name already registered.")
            return False

        # Check if phone address already exists
        if self.phone_address.data in (school.phone_address for school in storage.all('School').values()):
            self.phone_address.errors.append("Phone address already registered.")
            return False

        # Check if password is already used
        passwords_ = [school.password for school in storage.all('School').values()]
        for password_ in passwords_:
            if bcrypt.check_password_hash(password_, self.password.data):
                self.password.errors.append("Password already used.")
                return False

        return True


class CreateClass(FlaskForm):
    name = StringField('Class name', validators=[DataRequired(), Length(max=40)])
    submit = SubmitField("Create")

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        from models.engine import storage
        from models.sch_acc import Classes
        session = storage.session()
        classes = session.query(Classes).all()
        for class_ in classes:
            if class_.name == self.name and current_user.name == class_.school.name:
                self.name.errors.append('This already class exist')
                raise False
        return True
