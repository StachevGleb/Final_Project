from flask import render_template, url_for, flash, redirect, request
from gallery import app, db, bcrypt
from gallery.forms import RegistrationForm, LoginForm, UpdateProfileForm, PostForm
from gallery.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user
from PIL import Image
import secrets
import os


@app.route("/")
@app.route("/posts")
def posts():
    post = Post.query.all()
    return render_template('posts.html', posts=post)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your profile created, please, log in !', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('posts'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('posts'))

def save_pic(form_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext =  os.path.splitext(form_pic.filename)
    pic_filename = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static/profile_img', pic_filename)

    resized_pic = (125, 125)
    img = Image.open(form_pic)
    img.thumbnail(resized_pic)
    img.save(pic_path)

    return pic_filename

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file = save_pic(form.profile_pic.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_img/' + current_user.image_file)
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created!', 'success')
        return redirect(url_for('posts'))
    return render_template('create_post.html', title='New Post', form=form)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

# @app.route("/post/<int:post_id>/update")
# def post(post_id):