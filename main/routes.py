from flask import render_template, flash, redirect, url_for, request, abort, Blueprint
from app.models import Lodgement

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    plans = Lodgement.query.order_by(Lodgement.date_created.desc()).paginate(per_page=3, page=page)
    return render_template('home.html', title='Home', plans=plans, legend='Home')


@main.route("/about")
def about():
    return render_template('about.html', title='About')