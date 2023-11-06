from app.auth import bp
from app.auth.forms import RegisterForm
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