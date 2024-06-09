# from flask import Blueprint, render_template, redirect, url_for, flash, session, g
# from models import db, User
# from sqlalchemy.exc import IntegrityError
# from users.forms import UserAddForm, LoginForm

# users_blueprint = Blueprint('users', __name__)

# @users_blueprint.route('/signup', methods=["GET", "POST"])
# def signup():
#     form = UserAddForm()
#     if form.validate_on_submit():
#         try:
#             user = User.signup(
#                 username=form.username.data,
#                 password=form.password.data,
#                 email=form.email.data,
#             )
#             db.session.commit()
#         except IntegrityError:
#             flash("Username already taken", 'danger')
#             return render_template('signup.html', form=form)
#         session['curr_user'] = user.id
#         return redirect(url_for('home'))
#     return render_template('signup.html', form=form)

# @users_blueprint.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.authenticate(form.username.data, form.password.data)
#         if user:
#             session['curr_user'] = user.id
#             flash(f"Hello, {user.username}!", "success")
#             return redirect(url_for('home'))
#         flash("Invalid credentials.", 'danger')
#     return render_template('login.html', form=form)

# @users_blueprint.route('/logout')
# def logout():
#     session.pop('curr_user')
#     flash('Successfully logged out', 'success')
#     return redirect(url_for('users.login'))
