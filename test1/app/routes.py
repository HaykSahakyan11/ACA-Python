import os
import secrets
from PIL import Image
from flask import render_template, url_for, redirect, flash, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',
                           posts=posts)


@app.route('/about0')
def about0():
    title = 'Flask About'
    names = ["John", 'Jane', 'Jack']
    return render_template('about0.html',
                           title=title, names=names)


@app.route('/about')
def about():
    title = 'About Page'
    return render_template('about.html',
                           title=title)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',
                           title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            nest_page = request.args.get('next')
            return redirect(nest_page) if nest_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',
                           title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def save_prof_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/account', methods=['POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        data_not_changed = (current_user.username != form.username.data)
        if not data_not_changed and not form.picture.data:
            flash("No changes", 'success')
        else:
            if data_not_changed:
                current_user.username = form.username.data
                current_user.email = form.email.data
            elif form.picture.data:
                picture_file = save_prof_picture(form.picture.data)
                current_user.image_file = picture_file
            db.session.commit()
            flash("Your account has been updated", 'success')
        return redirect(url_for('account_get'))

    return redirect(url_for('account_get'))


@app.route('/account', methods=['GET'])
@login_required
def account_get():
    form = UpdateAccountForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    image_file = url_for('static', filename=f'profile_pics/{current_user.image_file}')
    return render_template('account.html',
                           title='Account', image_file=image_file, form=form)
