from app.auth import bp
from app.auth.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.get_users'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('users.get_users'))
        except:
            flash('Registration failed.', 'error')

    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    print('loggedin?', current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('users.get_users'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user and user.check_password(form.password.data):
            login_user(user)
            print('current', current_user)
            flash('Login successful!', 'success')
            return redirect(url_for('users.get_users'))
        else:
            flash('Login failed.', 'error')

    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))