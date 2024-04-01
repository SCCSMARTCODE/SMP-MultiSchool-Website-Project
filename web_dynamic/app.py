import datetime
from os import environ
"""This should be removed ASAP"""
environ["DB_PASSWD"] = "smp_pass_master"
environ["DB_HOST"] = "localhost"
environ["DB_USER"] = "smp_master"
environ["DB_NAME"] = "smp_base_db"
environ["DB_TYPE"] = "db"
environ['SMP_GMAIL'] = 'sccsmart247@gmail.com'
environ['SMP_GMAIL_PW'] = 'jemw amml ymty cukm'
"""This should be removed ASAP"""

from flask import Flask, render_template, url_for, redirect, flash, request
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, logout_user, login_user, login_required
import os
from functools import wraps
from PIL import Image

app = Flask(__name__)
app.config["SECRET_KEY"] = 'fbd43ee7955231e282a702d6ad8208bd'
bcrypt = Bcrypt()
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from models.student import Student
    from models.sch_acc import School
    from models.engine import storage
    user = storage.session()
    if user.query(Student).filter_by(id=user_id).first():
        return user.query(Student).filter_by(id=user_id).first()
    elif user.query(School).filter_by(id=user_id).first():
        return user.query(School).filter_by(id=user_id).first()
    else:
        return redirect(url_for('login'))


login_manager.init_app(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


def school_admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'SCHOOL':
            # Redirect to unauthorized page or raise an exception
            return redirect(url_for('unauthorized'))
        return func(*args, **kwargs)
    return decorated_function


def student_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'STUDENT':
            # Redirect to unauthorized page or raise an exception
            return redirect(url_for('unauthorized'))
        return func(*args, **kwargs)
    return decorated_function


def smp_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'SMP_ADMIN':
            # Redirect to unauthorized page or raise an exception
            return redirect(url_for('unauthorized'))
        return func(*args, **kwargs)
    return decorated_function


@app.route('/home')
@app.route('/', strict_slashes=False)
def home():
    return render_template('unauth_template/home.html', title='homepage')


@app.route("/school-registration", methods=['GET', 'POST'])
def school_reg():
    if current_user and current_user.is_authenticated:
        if current_user.role == 'SCHOOL':
            return redirect(url_for('school_dash'))
        elif current_user.role == 'STUDENT':
            return redirect(url_for('student_dash'))
        elif current_user.role == 'SMP_ADMIN':
            return redirect(url_for('admin_dashboard1'))

    from forms.school_sign_up_form import SchoolRegistrationForm as ScReg
    from models.sch_acc import School
    from static.messages import message
    form = ScReg()
    if form.validate_on_submit():

        new_school = School(
            name=form.name.data.title(),
            address=form.address.data.upper(),
            gmail=form.gmail.data.lower(),
            phone_address=form.phone_address.data,
            role='SCHOOL',
            password=bcrypt.generate_password_hash(form.password.data)
        )
        new_school.save()
        mail = form.gmail.data
        validator = "SMP officials have"

        message = message('Welcome School', new_school.name)
        send_message(receiver_gmail=new_school.gmail, subject='SMP Notification', message=message)
        return redirect(url_for('pending_acc', mail=mail, validator=validator))

    return render_template('unauth_template/school_sign_in.html', form=form, title='School Registration')


@app.route("/student-registration", methods=['GET', 'POST'])
def student_reg():
    if current_user and current_user.is_authenticated:
        if current_user.role == 'SCHOOL':
            return redirect(url_for('school_dash'))
        elif current_user.role == 'STUDENT':
            return redirect(url_for('student_dash'))
        elif current_user.role == 'SMP_ADMIN':
            return redirect(url_for('admin_dashboard1'))

    from models.student import Student
    from forms.student_sign_up_form import StudentRegistrationForm as StReg, get_class
    from static.messages import message

    form = StReg()
    if form.validate_on_submit():
        from models.sch_acc import School
        from models.engine import storage

        session = storage.session()

        school_id = ''
        school_name = ''
        for y in get_class(0):
            if form.school.data == y[0]:
                school_name = y[1]
                break

        for x in get_class(1):
            if x[1] == school_name:
                school_id = x[0]
                break

        school = session.query(School).filter_by(id=school_id).first()
        if school.strict_registration:
            if form.gmail.data.lower() not in [user.gmail for user in school.strict_users]:
                flash(f'Sorry, you are not an authorized user. Please contact {school_name} administrator for assistance.', 'danger')
                return redirect(url_for('student_reg'))

        new_student = Student(
            first_name=form.first_name.data.title(),
            last_name=form.last_name.data.title(),
            school_id=school_id,
            role="STUDENT",
            gmail=form.gmail.data.lower(),
            password=bcrypt.generate_password_hash(form.password.data)
        )
        new_student.save()

        mail = form.gmail.data
        validator = ""
        for x, y in get_class(0):
            if x == int(form.school.data):
                validator = y + ' has'

        message = message('Welcome Student', new_student.first_name)
        send_message(receiver_gmail=new_student.gmail, subject='SMP Notification', message=message)

        return redirect(url_for('pending_acc', mail=mail, validator=validator))
    return render_template('unauth_template/student_sign_in.html', form=form, title='Student Registration')


@app.route("/login", methods=['GET', 'POST'])
def login():
    from forms.login_form import Login
    from models.engine import storage
    from static.messages import message
    form = Login()

    if current_user and current_user.is_authenticated:
        if current_user.role == 'SCHOOL':
            return redirect(url_for('school_dash'))
        elif current_user.role == 'STUDENT':
            return redirect(url_for('student_dash'))
        elif current_user.role == 'SMP_ADMIN':
            return redirect(url_for('admin_dashboard1'))

    if form.validate_on_submit():
        for user in storage.all('School').values():
            if user.gmail and user.password and form.gmail.data.lower() == user.gmail and bcrypt.check_password_hash(user.password, form.password.data):
                if user.status:
                    school_user = load_user(user.id)
                    login_user(school_user, remember=form.remember.data)
                    if current_user.role == 'SCHOOL':
                        return redirect('/School-Dashboard')
                    elif current_user.role == 'SMP_ADMIN':
                        return redirect(url_for('admin_dashboard1'))

                else:
                    message = message('inactive school', user.name)
                    send_message(receiver_gmail=user.gmail, subject='SMP Notification, Account Inactive', message=message)
                    flash('Login Unsuccessful, Your account is currently Inactive', 'success')
                    return redirect(url_for('login'))
        for user in storage.all('Student').values():
            if user.gmail and user.password and form.gmail.data.lower() == user.gmail and bcrypt.check_password_hash(user.password, form.password.data):
                if user.status:
                    student_user = load_user(user.id)
                    login_user(student_user, remember=form.remember.data)
                    return redirect(url_for('student_dash'))
                else:
                    message = message('inactive student', user.first_name)

                    send_message(receiver_gmail=user.gmail, subject='SMP Notification, Account Inactive', message=message)

                    flash('Login Unsuccessful, Your account is currently Inactive', 'success')
                    return redirect(url_for('login'))

        flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('unauth_template/login.html', form=form, title='User login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/about-us")
def about_us():
    return render_template('unauth_template/about_us.html', title='about-us')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    from datetime import datetime
    import json
    file_name = 'contact.json'

    if request.method == 'POST':
        gmail = request.form.get('gmail')
        name = request.form.get('name')
        message = request.form.get('message')
        time = datetime.now().isoformat()

        data = {
            "time": time,
            "gmail": gmail,
            "name": name,
            "message": message
        }

        try:
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    datas = json.load(f)
                datas.append(data)
            else:
                datas = [data]

            with open(file_name, 'w') as w:
                json.dump(datas, w, indent=4)
            flash('Message sent!', 'success')
        except Exception as e:
            flash(f"Error occurred: {e}", 'danger')

    return render_template('unauth_template/contact.html', title='contact')


@app.route("/pending_account/<mail>/<validator>")
def pending_acc(mail, validator):
    return render_template('unauth_template/pending_acc.html', title='Pending Account', mail=mail, validator=validator)


@app.route("/Admin_dashboard_active")
@login_required
@smp_required
def admin_dashboard1():
    from models.sch_acc import School
    from models.engine import storage
    session = storage.session()

    schools = session.query(School).filter_by(role='SCHOOL').all()
    return render_template('auth_template/smp_admin/dashboard_active.html', title='Admin dashboard1', schools=schools)


@app.route("/Admin_dashboard_inactive")
@login_required
@smp_required
def admin_dashboard2():
    from models.engine import storage
    return render_template('auth_template/smp_admin/dashboard_inactive.html', title='Admin dashboard2', schools=storage.all('School').values())


@app.route("/Admin_dashboard_manage_user", methods=['GET', 'POST'])
@login_required
@smp_required
def admin_dashboard3():
    from models.engine import storage
    from static.messages import message
    if request.method == 'POST':
        form_id = request.form.get('id')
        form_status = request.form.get('status')

        if form_id and form_status:
            schools = storage.all('School').values()
            for school in schools:
                if form_id == str(school.id):
                    try:
                        school.status = bool(int(form_status))
                        school.updated_at = datetime.datetime.now()
                        storage.save()

                        flash('School status updated successfully', 'success')
                        message = message('active school', school.name)
                        send_message(receiver_gmail=school.gmail, subject='SMP Notification, Account Activated', message=message)

                        return redirect(url_for('admin_dashboard3'))
                    except Exception as e:
                        flash('Error updating school status: {}'.format(str(e)), 'danger')
                        return redirect(url_for('admin_dashboard3'))
            else:
                flash('School not found', 'danger')
                return redirect(url_for('admin_dashboard3'))
        else:
            flash('Invalid form data', 'danger')
            return redirect(url_for('admin_dashboard3'))

    return render_template('auth_template/smp_admin/dashboard_manage_activeness.html', title='Admin dashboard3')


@app.route("/Admin_contact_notification")
@login_required
@smp_required
def admin_dashboard4():
    import json
    file_name = 'contact.json'
    notifications = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            notifications = json.load(f)

    return render_template('auth_template/smp_admin/contact_notification.html', title='Admin dashboard4', datas=notifications)


@app.route('/Student-Dashboard')
@login_required
@student_required
def student_dash():
    from models.engine import storage
    from models.school_test import SchoolFiles
    from models.student_result import StudentSubmit
    session = storage.session()
    resources = []
    results = []

    if current_user.class_:
        files = session.query(SchoolFiles).filter_by(class_id=current_user.class_.id, file_category='TEST').all()
        for resource in files:
            check = session.query(StudentSubmit).filter_by(student_id=current_user.id, test_id=resource.id).first()
            if not check:
                resources.append(resource)
            elif check:
                results.append((resource, check.score))

    return render_template('auth_template/student/student_dashboard.html', title='Dashboard', resources=resources, results=results, school_pic_name=get_school_pics(current_user.school))


@app.route('/Student-Profile', methods=['GET', 'POST'])
@login_required
@student_required
def student_profile():
    from models.sch_acc import ProfilePic
    from models.engine import storage

    session = storage.session()

    if request.method == 'POST':
        if save_profile_pic():
            return redirect(url_for('student_profile'))

    pic = session.query(ProfilePic).filter_by(user_id=current_user.id).first()
    if pic:
        pic_name = f'{pic.id}{pic.file_ext}'
    else:
        pic_name = 'default.png'
    return render_template('auth_template/student/student_profile.html', title="Profile", user=current_user, pic_name=pic_name, school_pic_name=get_school_pics(current_user.school))


def save_profile_pic():
    from models.sch_acc import ProfilePic
    from models.engine import storage

    session = storage.session()

    import os
    initial_pic = session.query(ProfilePic).filter_by(user_id=current_user.id).first()

    if initial_pic:
        temp_file_name = f'{current_user.id}{initial_pic.file_ext}'
        temp_path = f'static/Files/user_profile_pics/{temp_file_name}'
        init_file_name = f"{initial_pic.id}{initial_pic.file_ext}"
        init_path = f'static/Files/user_profile_pics/{init_file_name}'
        if os.path.exists(init_path):
            os.remove(init_path)
        request.files['profile_pic'].save(temp_path)

        saved_image = Image.open(temp_path)
        resized_image = saved_image.resize((203, 203))

        resized_image.save(init_path)

        os.remove(temp_path)
        return True
    else:
        picture = request.files['profile_pic']

        _, file_ext = os.path.splitext(picture.filename)

        temp_file_name = f'{current_user.id}{file_ext}'
        temp_path = f'static/Files/user_profile_pics/{temp_file_name}'

        new_pic = ProfilePic(
            user_id=current_user.id,
            file_ext=file_ext
        )
        session.add(new_pic)
        session.commit()

        new_file_name = f'{new_pic.user_id}{new_pic.file_ext}'
        new_path = f'static/Files/user_profile_pics/{new_file_name}'

        request.files['profile_pic'].save(temp_path)

        saved_image = Image.open(temp_path)
        resized_image = saved_image.resize((203, 203))

        resized_image.save(new_path)
        os.remove(temp_path)
        return True


@app.route('/Student-Notification')
@login_required
@student_required
def student_note():
    from models.engine import storage
    from models.student import Notification

    messages = []
    session = storage.session()
    if current_user.class_:
        messages = session.query(Notification).filter_by(class_id=current_user.class_.id, school_id=current_user.school.id).order_by(Notification.created_at).all()
    return render_template('auth_template/student/student_notification.html', title='Notification', messages=messages, school_pic_name=get_school_pics(current_user.school))


@app.route('/Student-Resources')
@login_required
@student_required
def student_resource():
    from models.engine import storage
    from models.school_test import SchoolFiles
    session = storage.session()
    resources = []
    if current_user.class_:
        resources = session.query(SchoolFiles).filter_by(class_id=current_user.class_.id, file_category='RESOURCES').all()

    return render_template('auth_template/student/student_resources.html', title='Resources', resources=resources, school_pic_name=get_school_pics(current_user.school))


@app.route('/Student-Submit', methods=['GET', 'POST'])
@login_required
@student_required
def student_submit():
    from models.engine import storage
    from models.school_test import SchoolFiles
    from models.student_result import StudentSubmit

    session = storage.session()
    dir_path = f'static/Files/{current_user.school.name}'.replace(' ', '_')
    if request.method == 'POST':

        if not session.query(StudentSubmit).filter_by(student_id=current_user.id, test_id=request.form.get('test_id')).first():

            file = request.files['submitted_file']
            _, file_ext = os.path.splitext(file.filename)

            new_submit = StudentSubmit(
                student_id=current_user.id,
                test_id=request.form.get('test_id'),
                file_ext=file_ext
            )
            file_name = new_submit.id + file_ext
            file_path = os.path.join(dir_path, file_name)
            file.save(file_path)
            session.commit()
            flash('Submission Successful', 'success')
        else:
            flash('This project solution as been submitted', 'danger')

    resources = []
    if current_user.class_:
        files = session.query(SchoolFiles).filter_by(class_id=current_user.class_.id, file_category='TEST').all()
        for resource in files:
            if not session.query(StudentSubmit).filter_by(student_id=current_user.id, test_id=resource.id).first():
                resources.append(resource)
    return render_template('auth_template/student/student_submit.html', title='Submit', resources=resources, school_pic_name=get_school_pics(current_user.school))


@app.route('/Student-view/<id_>')
@login_required
@student_required
def student_view(id_):
    from models.engine import storage
    from models.school_test import SchoolFiles

    session = storage.session()
    file = session.query(SchoolFiles).filter_by(id=id_).first()
    filename = id_ + file.file_ext

    school_name = f"{current_user.school.name}".replace(' ', '_')
    path = os.path.join('Files', school_name, filename).replace('\\', '/')
    desc = file.description

    return render_template('auth_template/student/student_view.html', title='View', path=path, desc=desc)


@app.route('/School-view/<id_>')
@login_required
@school_admin_required
def school_view(id_):
    from models.engine import storage
    from models.student_result import StudentSubmit

    session = storage.session()
    file = session.query(StudentSubmit).filter_by(id=id_).first()
    filename = id_ + file.file_ext

    school_name = f"{current_user.name}".replace(' ', '_')
    path = os.path.join('Files', school_name, filename).replace('\\', '/')
    desc = file.test.description

    return render_template('auth_template/student/student_view.html', title='View', path=path, desc=desc)


@app.route('/School-Dashboard', methods=['GET', 'POST'])
@login_required
@school_admin_required
def school_dash():
    from models.student import Student
    from models.sch_acc import Classes
    from models.school_test import SchoolFiles
    from models.engine import storage

    if request.method == 'POST':
        if save_profile_pic():
            return redirect(url_for('school_dash'))

    session = storage.session()

    active_student_count = session.query(Student).filter_by(school_id=current_user.id, status=True).count()
    inactive_student_count = session.query(Student).filter_by(school_id=current_user.id, status=False).count()
    class_count = session.query(Classes).filter_by(school_id=current_user.id).count()
    resources_count = session.query(SchoolFiles).filter_by(school_id=current_user.id, file_category='RESOURCES').count()
    test_count = session.query(SchoolFiles).filter_by(school_id=current_user.id, file_category='TEST').count()

    return render_template('auth_template/school_admin/school_admin_dashboard.html', title='Dashboard',
                           user=current_user,
                           active_student_count=active_student_count,
                           inactive_student_count=inactive_student_count,
                           class_count=class_count,
                           resources_count=resources_count,
                           test_count=test_count,
                           pic_name=get_school_pics()
                           )


@app.route('/School-Active_Students')
@login_required
@school_admin_required
def school_active_students():
    from models.engine import storage
    from models.student import Student
    session = storage.session()
    students = session.query(Student).filter_by(school_id=current_user.id).all()
    return render_template('auth_template/school_admin/active_student_status.html', title='Dashboard', students=students, pic_name=get_school_pics())


@app.route('/School-InActive_Students')
@login_required
@school_admin_required
def school_inactive_students():
    from models.engine import storage
    from models.student import Student

    session = storage.session()
    students = session.query(Student).filter_by(school_id=current_user.id).all()
    return render_template('auth_template/school_admin/inactive_student_status.html', title='Dashboard', students=students, pic_name=get_school_pics())


@app.route("/Manipulate_Student's-status", methods=['GET', 'POST'])
@login_required
@school_admin_required
def student_status_manipulator():
    from models.engine import storage
    from models.student import Student
    from models.sch_acc import Classes
    from models.school_test import SchoolFiles
    from models.student_result import StudentSubmit
    from static.messages import message
    session = storage.session()

    if request.method == 'POST':

        if request.form.get('score'):
            info = session.query(StudentSubmit).filter_by(student_id=request.form.get('student_id'), test_id=request.form.get('test_id')).first()
            if info:
                info.score = request.form.get('score')
                session.commit()
                flash('Score Updated', 'success')
            else:
                flash('Solution to this test is not Found', 'danger')
            return redirect(url_for('student_status_manipulator'))

        elif request.form.get('status'):
            id_ = request.form.get('id')
            student = session.query(Student).filter_by(id=id_).first()
            if student:
                student.status = int(request.form.get('status'))
                student.updated_at = datetime.datetime.now()
                session.commit()
                message = message('active student', student.first_name)
                send_message(receiver_gmail=student.gmail, subject='SMP Notification, Account Activated', message=message)
                flash('Successful Update', 'success')
                return redirect(url_for('student_status_manipulator'))
        elif request.form.get('info'):
            id_ = request.form.get('id')
            session = storage.session()
            student = session.query(Student).filter_by(id=id_).first()
            if student:
                if request.form.get('info') == 'first_name':
                    student.first_name = request.form.get('new_value').title()
                elif request.form.get('info') == 'last_name':
                    student.last_name = request.form.get('new_value').title()
                elif request.form.get('info') == 'gmail':
                    student.gmail = request.form.get('new_value').lower()
                if request.form.get('new_value'):
                    student.updated_at = datetime.datetime.now()
                    session.commit()
                    flash('Successful Update', 'success')

                flash('Unsuccessful Update', 'success')
                return redirect(url_for('student_status_manipulator'))

        elif request.form.get('class'):
            id_ = request.form.get('id')
            student = session.query(Student).filter_by(id=id_).first()
            if student:
                student.class_id = request.form.get('class')
                student.updated_at = datetime.datetime.now()
                session.commit()
                flash('Class Updated', 'success')
                return redirect(url_for('student_status_manipulator'))
        else:
            flash('Unsuccessful Update', 'danger')
    classes = session.query(Classes).filter_by(school_id=current_user.id).all()
    score_range = [x / 2 for x in range(2, 201)]
    tests = session.query(SchoolFiles).filter_by(school_id=current_user.id, file_category='TEST')
    return render_template('auth_template/school_admin/student_status_manipulator.html', title='Dashboard', classes=classes, score_range=score_range, tests=tests, pic_name=get_school_pics())


@app.route('/School-Classes', methods=['GET', 'POST'])
@login_required
@school_admin_required
def school_classes():
    from web_dynamic.forms.school_sign_up_form import CreateClass
    from models.engine import storage
    from models.sch_acc import Classes
    form = CreateClass()
    session = storage.session()
    if form.validate_on_submit():
        if not session.query(Classes).filter_by(name=form.name.data, school_id=current_user.id).first():
            new_class = Classes(name=form.name.data, school_id=current_user.id)
            session = storage.session()
            session.add(new_class)
            session.commit()

            # classes = session.query(Classes).filter_by(school_id=current_user.id).all()
            flash('Class created successfully', 'success')
        else:
            flash('Class already exist', 'danger')
        return redirect(url_for('school_classes'))
    session = storage.session()
    classes = session.query(Classes).filter_by(school_id=current_user.id).all()
    return render_template('auth_template/school_admin/school_classes.html', title='Classes', form=form, classes=classes, pic_name=get_school_pics())


@app.route('/School-Uploaded-Files', methods=['GET', 'POST'])
@login_required
@school_admin_required
def school_uploaded_files():
    from models.school_test import SchoolFiles
    from models.engine import storage

    session = storage.session()
    files = session.query(SchoolFiles).filter_by(school_id=current_user.id).all()
    return render_template('auth_template/school_admin/school_uploaded_files.html', title='Resources', files=files, pic_name=get_school_pics())


@app.route('/School-Control-Registration', methods=['GET', 'POST'])
@login_required
@school_admin_required
def school_control_registration():
    from models.engine import storage
    from models.sch_acc import School, SchoolStrictUsers

    session = storage.session()
    if request.method == 'POST':

        school = session.query(School).filter_by(id=current_user.id).first()
        mode = request.form.get('registration_mode')
        new_auth_user = request.form.get('authorized_user_gmail')
        if mode:
            school.strict_registration = int(mode)
            session.commit()
            return redirect(url_for('school_control_registration'))
        elif new_auth_user:
            action = request.form.get('action')

            if action == 'add':
                ex_strict_user = session.query(SchoolStrictUsers).filter_by(school_id=current_user.id, gmail=request.form.get('authorized_user_gmail').strip()).first()
                if not ex_strict_user:
                    new_strict_user = SchoolStrictUsers(
                        gmail=request.form.get('authorized_user_gmail').strip(),
                        school_id=current_user.id
                    )
                    session.add(new_strict_user)
                    session.commit()
                    flash('Account info upload Successful', 'success')
                else:
                    flash('User exists', 'danger')
                return redirect(url_for('school_control_registration'))
            elif action == 'remove':
                ex_strict_user = session.query(SchoolStrictUsers).filter_by(school_id=current_user.id, gmail=request.form.get('authorized_user_gmail').strip()).first()
                if ex_strict_user:
                    session.delete(ex_strict_user)
                    session.commit()
                    flash('Deleted successfully', 'success')
                else:
                    flash("User doesn't exist", 'danger')
                return redirect(url_for('school_control_registration'))

    strict_users = session.query(SchoolStrictUsers).filter_by(school_id=current_user.id).all()
    mode = current_user.strict_registration
    return render_template('auth_template/school_admin/school_control_registration.html', title='Control-Registration', mode=mode, strict_users=strict_users, pic_name=get_school_pics())


@app.route('/Send-Notification', methods=['GET', 'POST'])
@login_required
@school_admin_required
def school_send_notification():
    from models.engine import storage
    from models.student import Notification
    from models.sch_acc import Classes

    session = storage.session()

    if request.method == 'POST':

        new_message = Notification(
            school_id=current_user.id,
            class_id=request.form.get('class_id'),
            message=request.form.get('message')
        )
        session.add(new_message)
        session.commit()
        flash('Notification Sent!', 'success')
        return redirect(url_for('school_send_notification'))

    classes = session.query(Classes).filter_by(school_id=current_user.id).all()
    return render_template('auth_template/school_admin/school_send_notification.html', title='Notification', classes=classes, pic_name=get_school_pics())


@app.route('/School-Submitted-test', methods=['GET', 'POST'])
@login_required
@school_admin_required
def submitted_test_info():
    # from models.student_result import StudentSubmit
    from models.school_test import SchoolFiles
    from models.engine import storage

    session = storage.session()

    datas = session.query(SchoolFiles).filter_by(school_id=current_user.id, file_category='TEST').all()
    if not datas:
        datas = []
    print(datas)
    return render_template('auth_template/school_admin/submitted_test_info.html', title='Submitted-Test', datas=datas, pic_name=get_school_pics())


@app.route('/School-Uploads', methods=['GET', 'POST'])
@login_required
@school_admin_required
def school_upload():
    from models.engine import storage
    from models.school_test import SchoolFiles
    if request.method == 'POST':
        dir_path = f'static/Files/{current_user.name}'.replace(' ', '_')

        if not request.form.get('id'):
            file = request.files['file']
            _, file_ext = os.path.splitext(file.filename)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            print(request.form.get('class'))
            new_file = SchoolFiles(
                school_id=current_user.id,
                description=request.form.get('description'),
                class_id=request.form.get('class'),
                file_ext=file_ext,
                file_category=request.form.get('file_type')
            )

            filename = f'{new_file.id}{file_ext}'
            file_path = os.path.join(dir_path, filename)
            file.save(file_path)
            storage.save()
            flash('Upload Successful', 'success')
            return redirect(url_for('school_upload'))
        else:
            session = storage.session()
            file = session.query(SchoolFiles).filter_by(id=request.form.get('id')).first()
            if file and current_user.id == file.school_id:
                file_path = os.path.join(dir_path, f'{file.id}{file.file_ext}')
                os.remove(file_path)
                session.delete(file)
                storage.save()
                flash('File Delete Successful', 'success')
                return redirect(url_for('school_upload'))
            else:
                flash('File not found Error!', 'danger')
                return redirect(url_for('school_upload'))

    return render_template('auth_template/school_admin/school_upload_delete.html', title='Uploads', pic_name=get_school_pics())


@app.route('/unauthorized')
def unauthorized():
    flash('You are not authorized to access this page.', 'danger')
    return redirect(url_for('home'))


def get_school_pics(user=current_user):
    from models.engine import storage
    from models.sch_acc import ProfilePic

    session = storage.session()
    pic = session.query(ProfilePic).filter_by(user_id=user.id).first()
    if pic:
        pic_name = f'{pic.id}{pic.file_ext}'
    else:
        pic_name = 'school_default.png'

    return pic_name


def send_message(receiver_gmail, subject, message):
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()

    SMP_GMAIL = os.getenv('SMP_GMAIL')
    SMP_GMAIL_PW = os.getenv('SMP_GMAIL_PW')

    msg['Subject'] = subject
    msg['From'] = SMP_GMAIL
    msg['To'] = receiver_gmail
    msg.set_content(message, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SMP_GMAIL, SMP_GMAIL_PW)
        smtp.send_message(msg)


if __name__ == '__main__':
    app.run(debug=True)
