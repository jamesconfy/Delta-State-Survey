from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, ValidationError
from datetime import date


class LodgementForm(FlaskForm):
    name_of_survey = StringField('Name of Survey', validators=[DataRequired()])
    full_name = StringField('Name of Surveyor')
    prefix = StringField('Prefix')
    plan_no = StringField('Plan Number', validators=[DataRequired()])
    location = StringField('Location of Survey', validators=[DataRequired()])
    purpose_of_survey = StringField('Purpose of Survey', validators=[DataRequired()])
    date_of_survey = DateField('Date of Survey', validators=[DataRequired()])
    area_of_land = StringField('Area of Land', validators=[DataRequired()])
    lodegement_fee = StringField('Lodgement Fee', validators=[DataRequired()])
    plan_file = FileField('Plan File', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit')

    def validate_date_of_survey(self, date_of_survey):
        current_date = date.today()
        if date_of_survey.data > current_date:
            raise ValidationError('Date cannot be greater than current date')

class ModificationForm(FlaskForm):
    name_of_survey = StringField('Name of Survey', validators=[DataRequired()])
    full_name = StringField('Name of Surveyor')
    prefix = StringField('Prefix')
    plan_no = StringField('Plan Number', validators=[DataRequired()])
    location = StringField('Location of Survey', validators=[DataRequired()])
    purpose_of_survey = StringField('Purpose of Survey', validators=[DataRequired()])
    date_of_survey = DateField('Date of Survey', validators=[DataRequired()])
    area_of_land = StringField('Area of Land', validators=[DataRequired()])
    lodegement_fee = StringField('Lodgement Fee', validators=[DataRequired()])
    plan_file = FileField('Plan File', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit')

    def validate_date_of_survey(self, date_of_survey):
        current_date = date.today()
        if date_of_survey.data > current_date:
            raise ValidationError('Date cannot be greater than current date')        