import os
import secrets
from datetime import date
from PIL import Image
from flask_login.utils import login_required, logout_user
from sqlalchemy import desc
from app.models import db
from flask import render_template, flash, redirect, url_for, request, abort
from app import app, bcrypt
from app.forms import LoginForm, RegistrationForm, UpdateAccountForm, LodgementForm, ModificationForm
from app.models import User, Lodgement
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    plans = Lodgement.query.order_by(Lodgement.date_of_survey.desc()).paginate(per_page=3, page=page)
    return render_template('home.html', title='Home', plans=plans)

@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
            else:
                flash('Login Unsucessful, check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        full_name = form.first_name.data + ' ' + form.last_name.data
        user = User(username=form.username.data, email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data, full_name=full_name, password=hashed_password, location=form.location.data, prefix=form.prefix.data, phone_no=form.phone_no.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

def save_picture(form_picture):
    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn

def save_plan_image(form_picture):
    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/plan_image', picture_fn)

    output_size = (500, 500)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn

@app.route("/account", methods=['POST', 'GET'])
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
            return redirect(url_for('account'))

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

@app.route("/plan_lodgement", methods=['POST', 'GET'])
@login_required
def plan_lodgement():
    form = LodgementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            plan_image = form.plan_file.data
            if plan_image:
                plan_image1 = save_plan_image(form.plan_file.data)

            logdement = Lodgement(name_of_survey=form.name_of_survey.data, prefix=current_user.prefix, plan_no=form.plan_no.data, location=form.location.data, purpose_of_survey=form.purpose_of_survey.data, date_of_survey=form.date_of_survey.data, area_of_land=form.area_of_land.data, lodegement_fee=form.lodegement_fee.data, plan_file=plan_image1, surveyor=current_user)
            db.session.add(logdement)
            db.session.commit()
            flash('Lodgement Added', 'success')
            return redirect(url_for('plan_lodgement'))

    form.prefix.data = current_user.prefix
    form.full_name.data = current_user.full_name
    return render_template('plan_lodgement.html', title='Plan Lodgement', form=form, legend='New Lodgement')

@app.route("/record")
@login_required
def record():
    plans = Lodgement.query.order_by(Lodgement.date_of_survey.desc()).filter_by(user_id=current_user.id)
    return render_template('record.html', title='Record', plans=plans)

@app.route("/record/<int:plan_id>")
def record_view(plan_id):
    plan = Lodgement.query.get_or_404(plan_id)
    return render_template('spec_record.html', plan=plan, title=plan.plan_no)


@app.route("/record/<int:plan_id>/modify", methods=['GET', 'POST'])
@login_required
def modify(plan_id):
    plan = Lodgement.query.get_or_404(plan_id)
    if plan.surveyor != current_user:
        abort(404)
    
    form = ModificationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            plan_image = form.plan_file.data
            if plan_image:
                plan_image2 = save_plan_image(form.plan_file.data)
            else:
                plan_image2 = plan.plan_file

            plan.name_of_survey = form.name_of_survey.data
            plan.plan_no = form.plan_no.data
            plan.location = form.location.data
            plan.purpose_of_survey = form.purpose_of_survey.data
            plan.date_of_survey = form.date_of_survey.data
            plan.area_of_land = form.area_of_land.data
            plan.lodegement_fee = form.lodegement_fee.data
            plan.plan_file = plan_image2
            db.session.commit()
            flash('Your Lodgement have been updated successfully', 'success')
            return redirect(url_for('record_view', plan_id=plan.id))

    elif request.method == 'GET':
        form.name_of_survey.data = plan.name_of_survey
        form.full_name.data = plan.surveyor.full_name
        form.prefix.data = plan.surveyor.prefix
        form.plan_no.data = plan.plan_no
        form.location.data = plan.location
        form.purpose_of_survey.data = plan.purpose_of_survey
        form.date_of_survey.data = plan.date_of_survey
        form.area_of_land.data = plan.area_of_land
        form.lodegement_fee.data = plan.lodegement_fee
        form.plan_file.data = plan.plan_file
    return render_template('plan_lodgement.html', title='Modify', form=form, legend='Update Lodgement')


@app.route("/record/<int:plan_id>/delete", methods=['POST'])
@login_required
def delete(plan_id):
    plan = Lodgement.query.get_or_404(plan_id)
    if plan.surveyor != current_user:
        abort(404)

    db.session.delete(plan)
    db.session.commit()

    flash('Your Lodgement have been deleted successfully', 'danger')
    return redirect(url_for('record'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
