# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from wtforms.fields.html5 import EmailField
from app.validators import Unique
from app.models import User

class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=8, max=16),
            Unique(User, User.username, "Username already in use")
        ]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    email = EmailField(
        "Email", validators=[
            DataRequired(),
            Email(),
            Unique(User, User.email, "Email already in use")
        ]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=8, max=16)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=16)]
    )
    submit = SubmitField("Sign In")

