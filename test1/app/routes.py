import os
import secrets
from PIL import Image
from flask import render_template, url_for, redirect, flash, request, abort
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm
from app.models import User, Post, Comments
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
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
def account_post():
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


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html',
                           title='New Post', form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',
                           title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',
                           title='Update Post', form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('index'))


@app.route("/comment", methods=['POST','GET'])
@login_required
def comment():
    print("***************************************")
    form = CommentForm()
    #print(help(form))
    #print(dir(form))
    if form.is_submitted():
        #print("000000000000000000000000000")
        print(form.content.data)
        print(current_user.id, '//////////////////')
        print(current_user.username, '//////////////////////////////////')
        comment = Comments(content=form.content.data, author=current_user)
        db.session.add(comment)
        db.session.commit()

    #flash('Your post has been deleted!', 'success')
    return render_template('comments.html', form=form)
    #return "*******************"


@app.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query\
        .filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('user_posts.html',
                           posts=posts, user=user)