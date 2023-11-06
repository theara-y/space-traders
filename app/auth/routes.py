from app.auth import bp
from app.auth.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from flask import render_template, redirect, url_for, flash

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('users.get_users'))

    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_404()
        print(user.password)
        if user.check_password(form.password.data):
            flash('Login successful!')
            return redirect(url_for('users.get_users'))
        else:
            flash('Login failed.')

    return render_template('auth/login.html', form=form)