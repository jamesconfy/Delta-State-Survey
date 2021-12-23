from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password Must Match')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    prefix = StringField('Prefix')
    location = StringField('Location')
    phone_no = StringField('Phone Number', validators=[Regexp(regex="^((\+234|0)[7-9][0-1]\d{8}$)|^()", message="Invalid Number")])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists')

    
    def validate_phone_no(self, phone_no):
        numb = phone_no.data
        if len(numb) == 14:
            numb1 = numb[0:6]
            if numb1 != "+23470":
                if numb1 != "+23480":
                    if numb1 != "+23490":
                        if numb1 != "+23481":
                            if numb1 != "+23491":
                                raise ValidationError('Invalid Phone Number, Number should start with +23470/+23480/+23490/+23481')

        elif len(numb) == 11:
            numb1 = numb[0:3]
            if numb1 != "070":
                if numb1 != "080":
                    if numb1 != "090":
                        if numb1 != "081":
                            if numb1 != "091":
                                raise ValidationError('Invalid Phone Number, Number should start with 070/080/090/081')
        
        elif len(numb) >= 15 or len(numb) <= 10:
            if len(numb) >= 1:
                raise ValidationError('Number Should be in format +234XXXXXXXXXX or 0XXXXXXXXXX')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    prefix = StringField('Prefix')
    location = StringField('Location')
    phone_no = StringField('Phone Number', validators=[Regexp(regex="^((\+234|0)[7-9][0-1]\d{8}$)|^()", message="Invalid Number")])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username already exists')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exists')

    
    def validate_phone_no(self, phone_no):
        if phone_no.data != current_user.phone_no:
            numb = phone_no.data
            if len(numb) == 14:
                numb1 = numb[0:6]
                if numb1 != "+23470":
                    if numb1 != "+23480":
                        if numb1 != "+23490":
                            if numb1 != "+23481":
                                if numb1 != "+23491":
                                    raise ValidationError('Invalid Phone Number, Number should start with +23470/+23480/+23490/+23481')

            elif len(numb) == 11:
                numb1 = numb[0:3]
                if numb1 != "070":
                    if numb1 != "080":
                        if numb1 != "090":
                            if numb1 != "081":
                                if numb1 != "091":
                                    raise ValidationError('Invalid Phone Number, Number should start with 070/080/090/081')
        
            elif len(numb) >= 15 or len(numb) <= 10:
                if len(numb) >= 1:
                    raise ValidationError('Number Should be in format +234XXXXXXXXXX or 0XXXXXXXXXX')

            numb = User.query.filter_by(phone_no=phone_no.data).first()
            if numb:
                raise ValidationError('This number is taken')
