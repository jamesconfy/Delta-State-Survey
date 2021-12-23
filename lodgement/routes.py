from flask_login.utils import login_required
from app.models import db
from flask import render_template, flash, redirect, url_for, request, abort, Blueprint
from lodgement.forms import LodgementForm, ModificationForm
from app.models import User, Lodgement
from flask_login import current_user, login_required
from lodgement.utils import save_plan_image


lodgement = Blueprint('lodgement', __name__)


@lodgement.route("/plan_lodgement", methods=['POST', 'GET'])
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
            return redirect(url_for('lodgement.plan_lodgement'))

    form.prefix.data = current_user.prefix
    form.full_name.data = current_user.full_name
    return render_template('plan_lodgement.html', title='Plan Lodgement', form=form, legend='New Lodgement')

@lodgement.route("/record/<int:user_id>")
def record(user_id):
    user = User.query.filter_by(id=user_id).first()
    plans = Lodgement.query.order_by(Lodgement.date_of_survey.desc()).filter_by(user_id=user_id)
    return render_template('record.html', title='Record', plans=plans, user=user, legend='Record')

@lodgement.route("/record/<string:name>/<int:plan_id>")
def record_view(name, plan_id):
    plan = Lodgement.query.get_or_404(plan_id)
    return render_template('spec_record.html', plan=plan, title=plan.plan_no, legend='Specific Records')


@lodgement.route("/record/<string:name>/<int:plan_id>/modify", methods=['GET', 'POST'])
@login_required
def modify(name, plan_id):
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
            return redirect(url_for('lodgement.record_view', plan_id=plan.id))

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


@lodgement.route("/record/<int:plan_id>/delete", methods=['POST'])
@login_required
def delete(plan_id):
    plan = Lodgement.query.get_or_404(plan_id)
    if plan.surveyor != current_user:
        abort(404)

    db.session.delete(plan)
    db.session.commit()

    flash('Your Lodgement have been deleted successfully', 'danger')
    return redirect(url_for('lodgement.record'))
