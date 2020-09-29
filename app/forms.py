from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class TokenListForm(FlaskForm):
    limit = IntegerField('Limit', validators=[DataRequired()])    
    submit = SubmitField('Search')

class SimilarityForm(FlaskForm):
    token = StringField('Token', validators=[DataRequired()])
    limit = IntegerField('Limit', validators=[DataRequired()])    
    search = SubmitField('Search')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

