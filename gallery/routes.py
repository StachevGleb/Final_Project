import psycopg2
from flask import render_template, url_for, flash, redirect, request
from gallery import app, db, bcrypt, mail
from gallery.forms import RegistrationForm, LoginForm, UpdateProfileForm, PostForm, \
    RequestResetForm, ResetPasswordForm, UploadPaintingForm
from gallery.models import User, Post, Artist, Painting
from flask import abort
from flask_login import login_user, logout_user, login_required, current_user
from PIL import Image
import secrets
import os
from flask_mail import Message



#############################
# from gallery.painting_db import save_artist, save_painting



@app.route("/")
@app.route("/posts")
def posts():
    page = request.args.get('page', 1, type=int)
    posted = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    # save_artist()
    # save_painting()
    return render_template('posts.html', posted=posted)


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


# correct saving of profile img (size)
def save_pic(form_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pic.filename)
    pic_filename = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static/profile_img', pic_filename)

    target_height = 325
    img = Image.open(form_pic)
    aspect_ratio = img.width / img.height
    target_width = int(target_height * aspect_ratio)
    resized_pic = (target_width, target_height)
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
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


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
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('posts'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posted = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('user_posts.html', posted=posted, user=user)


# sending email

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500


@app.route("/artists")
def artists():
    page = request.args.get('page', 1, type=int)
    art_list = Artist.query.order_by(Artist.id.asc()).paginate(page=page, per_page=3)

    return render_template('artists.html', art_list=art_list)


@app.route("/paintings")
def paintings():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="gallery",
        user="postgres",
        password="Lena091165"
    )
    cursor = conn.cursor()
    query = "SELECT id FROM artist"

    cursor.execute(query)
    results = cursor.fetchall()  # Retrieve all rows
    images_list = []
    images_list_rel = []
    for row in results:
        id_value = row[0]
        image_list = os.listdir('gallery/static/paintings' + '/' + str(id_value))
        image_list = [str(id_value) + '/' + image for image in image_list]
        images_list.append(image_list)

        for image in image_list:
            my_new_string = image.replace(".jpg", "")
            my_new_string = my_new_string.replace("/", '').lstrip('0123456789')
            images_list_rel.append(my_new_string)

    cursor.close()
    conn.close()

    page = request.args.get('page', 1, type=int)
    paint_list = Painting.query.order_by(Painting.id.asc()).paginate(page=page, per_page=6)

    return render_template('paintings.html', paint_list=paint_list, images_list_rel=images_list_rel)


# def save_pic(form_pic):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_pic.filename)
#     pic_filename = random_hex + f_ext
#     pic_path = os.path.join(app.root_path, 'static/profile_img', pic_filename)
#
#
#     target_height = 325
#     img = Image.open(form_pic)

#     aspect_ratio = img.width / img.height
#     target_width = int(target_height * aspect_ratio)
#     resized_pic = (target_width, target_height)
#     img.thumbnail(resized_pic)
#     img.save(pic_path)
#
#     return pic_filename
def save_painting(painting_img, painting_name, artist_id, counter):
    _, f_ext = os.path.splitext(painting_img.filename)
    pic_filename = painting_name + f_ext
    dir_path = os.path.join(app.root_path, 'static/paintings/')
    dir_name = str(artist_id)
    path = os.path.join(dir_path, dir_name)
    if counter == 0:
        os.mkdir(path)
    pic_path = os.path.join(path + '/' + pic_filename)

    target_height = 700
    img = Image.open(painting_img)
    aspect_ratio = img.width / img.height
    target_width = int(target_height * aspect_ratio)
    resized_pic = (target_width, target_height)
    img.thumbnail(resized_pic)
    img.save(pic_path)

    return pic_filename


@app.route("/upload_painting", methods=['GET', 'POST'])
@login_required
def upload_painting():
    form = UploadPaintingForm()
    if form.validate_on_submit():
        if form.painting_img.data:
            artists_list = Artist.query.all()
            for artist in artists_list:
                painting_name = form.description.data
                artist_id = artist.id
                painting_img = form.painting_img.data
                if artist.artistname == current_user.username:
                    artist = Artist(artistname=current_user.username, about=form.about.data)
                    db.session.add(artist)
                    db.session.commit()
                    painting = Painting(title=current_user.username, description=form.description.data,
                                        artist_id=artist.id)
                    db.session.add(painting)
                    db.session.commit()
                    save_painting(painting_img, painting_name, artist_id, counter=0)
                    flash('Artist with your current user name has been created and painting uploaded!', 'success')
                    return redirect(url_for('paintings'))
                else:
                    artist = Artist.query.filter_by(artistname=current_user.username).first()
                    artist_id = artist.id
                    painting = Painting(title=current_user.username, description=form.description.data,
                                        artist_id=artist.id)
                    db.session.add(painting)
                    db.session.commit()
                    save_painting(painting_img, painting_name, artist_id, counter=1)
                    flash('Additional painting uploaded!', 'success')
                    return redirect(url_for('paintings'))
    artists_list = Artist.query.all()
    paint_file = ''
    for artist in artists_list:
        painting = Painting.query.filter_by(artist_id=artist.id).first()
        if current_user.username == artist.artistname:
            paint_file = url_for('static', filename='paintings/' + str(artist.id) + '/' + painting.description)
    return render_template('upload_painting.html', title='Upload Painting', paint_file=paint_file, form=form)


@app.route("/match_artists_game")
def match_artists():
    return render_template('match_game.html')
