# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, current_user
from app.forms import RegisterForm, LoginForm
from app.models import db, User

users = Blueprint("users", __name__)
login_manager = LoginManager()

def redirect_dest(fallback):
    next = request.args.get("next")
    try:
        dest_url = url_for(next)
    except:
        dest_url = url_for(fallback)
    return redirect(dest_url)


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Register successfully")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user:
            user.check_password(form.password.data)
            login_user(user)
            return redirect_dest("home.html")
        flash("Username or password invalid")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
def logout():
    logout_user()
    flash("Logged successfully")
    return redirect(url_for("users.login"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def handler_needs_login():
    flash("This page require authentication")
    return redirect(url_for("users.login", next=request.endpoint))

