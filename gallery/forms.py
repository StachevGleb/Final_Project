from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from gallery.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed, FileRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_name(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This name already exist, please, take another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exist, please, take another one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    profile_pic = FileField('Upload your profile picture (only .png and .jpg)',
                            validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_name(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This name already exist, please, take another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exist, please, take another one')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request to reset password')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no profile with this email. First you should sing up.')


# sending email

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset password')


# Uploading paintings
class UploadPaintingForm(FlaskForm):
    about = StringField('Two sentences about yourself (You like a painter)',
                        validators=[Length(max=100)])
    description = StringField('Short name of your painting',
                              validators=[DataRequired(), Length(min=2, max=100)])
    painting_img = FileField('Upload your painting (only .png and .jpg)', validators=[
        FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')


class UpdatingPaintingForm(FlaskForm):
    description = StringField('Short updated name of your painting',
                              validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Upload')


