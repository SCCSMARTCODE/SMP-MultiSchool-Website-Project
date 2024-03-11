from os import environ
"""This should be removed ASAP"""
environ["DB_PASSWD"] = "smp_pass_master"
environ["DB_HOST"] = "localhost"
environ["DB_USER"] = "smp_master"
environ["DB_NAME"] = "smp_base_db"
environ["DB_TYPE"] = "db"
"""This should be removed ASAP"""

from flask import Flask, render_template, url_for, redirect, flash
from forms.login_form import Login
from forms.school_sign_up_form import SchoolRegistrationForm as ScReg
from forms.student_sign_up_form import StudentRegistrationForm as StReg


app = Flask(__name__)
app.config["SECRET_KEY"] = 'fbd43ee7955231e282a702d6ad8208bd'


@app.route('/home')
@app.route('/', strict_slashes=False)
def home():
    return render_template('unauth_template/home.html', title='homepage')


@app.route("/school-registration", methods=['GET', 'POST'])
def school_reg():
    form = ScReg()
    if form.validate_on_submit():
        mail = form.gmail.data
        return redirect(url_for('pending_acc', mail=mail))
    else:
        flash("Account creation failed...", 'failed')
    return render_template('unauth_template/school_sign_in.html', form=form, title='School Registration')


@app.route("/student-registration", methods=['GET', 'POST'])
def student_reg():
    form = StReg()
    return render_template('unauth_template/student_sign_in.html', form=form, title='Student Registration')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('', form=form, title='Login')


@app.route("/about-us")
def about_us():
    return render_template('unauth_template/about_us.html', title='about-us')


@app.route("/pending account")
def pending_acc(mail):
    return render_template('unauth_template/pending_acc.html', title='Pending Account', mail=mail)


@app.route("/dashboard")
def student_dashboard():
    pass


if __name__ == '__main__':
    app.run(debug=True)
