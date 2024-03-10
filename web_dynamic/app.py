from flask import Flask, render_template, url_for
from forms.login_form import Login
from forms.school_sign_up_form import SchoolRegistrationForm as sc_reg
from forms.student_sign_up_form import StudentRegistrationForm as st_reg

app = Flask(__name__)
app.config["SECRET_KEY"] = 'fbd43ee7955231e282a702d6ad8208bd'


@app.route("/school-registration")
def school_reg():
    return render_template(url_for('/unauth_template.school_sign_in.html'))
