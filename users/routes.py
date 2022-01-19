from app.models import db
from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import bcrypt
from users.forms import LoginForm, RegistrationForm, UpdateAccountForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from users.utils import save_picture


users = Blueprint('users', __name__)


@users.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                next_url = request.form.get('next')
                if next_url:
                    return redirect(next_url)
            else:
                flash('Login Unsucessful, check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            full_name = form.first_name.data + ' ' + form.last_name.data
            user = User(username=form.username.data, email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data, full_name=full_name, password=hashed_password, location=form.location.data, prefix=form.prefix.data, phone_no=form.phone_no.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully for {form.username.data}', 'success')
            return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/account", methods=['POST', 'GET'])
@login_required
def account():
    form = UpdateAccountForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file

            current_user.username = form.username.data
            current_user.email = form.email.data
            current_user.phone_no = form.phone_no.data
            current_user.prefix = form.prefix.data
            current_user.location = form.location.data
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            db.session.commit()
            flash('Your account have been updated successfully', 'success')
            return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone_no.data = current_user.phone_no
        form.prefix.data = current_user.prefix
        form.location.data = current_user.location
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name

    image_file = url_for('static', filename=f'profile_pics/{current_user.image_file}')
    return render_template('account.html', title='Account', form=form, image_file=image_file)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
