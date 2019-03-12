# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, url_for, render_template, abort, flash
from flask_login import LoginManager, login_user, logout_user, current_user
from app.forms import RegisterForm, LoginForm
from app.models import db, User, Link
from app.mail import send_mail

users = Blueprint("users", __name__)
login_manager = LoginManager()

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = User(username, password, email)
        user.generate_activate_link()
        db.session.add(user)
        db.session.commit()
        flash("Activate your account with the activation link sent to the registered email")
        context = {
            "username": username,
            "token": user.link.token
        }
        send_mail(
            subject="Active account",
            recipients=[user.email],
            context=context,
            body_template="active_account.txt",
            html_template="active_account.html"
        )
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(form.password.data):
            if user.is_activated:
                login_user(user)
                flash("Login successfully")
                return redirect(url_for("index"))
            else:
                flash("Email not confirmed verify link of activation in your email")
        else:
            flash("Username or password invalid")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
def logout():
    logout_user()
    flash("Logout successfully")
    return redirect(url_for("users.login"))


@users.route("/active_account/<token>")
def active_account(token):
    link = Link.query.filter_by(token=token).first()
    if not link:
        abort(404)
    link.user.is_activated = True
    login_user(link.user)
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for("index"))


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def needs_authentication():
    flash("This page require authentication.")
    return redirect(url_for("users.login"))

