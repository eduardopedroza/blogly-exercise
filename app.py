"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SECRET!"

@app.route('/')
def index():
    return redirect('/users')
    

@app.route('/users')
def show_users():

    users = User.query.all()
    return render_template("user_listing.html", users=users)

@app.route('/users/new', methods=['GET'])
def new_user_form():
    return render_template("new_user_form.html")

@app.route('/users/new', methods=['POST'])
def add_user():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    image_url = request.form['imageURL'] or None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)    
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>', methods=['GET'])
def show_user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def show_edit_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['firstName']
    user.last_name = request.form['lastName']
    user.image_url = request.form['imgURL'] or None
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/posts/new', methods=['GET'])
def show_new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("new_post.html", user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_new_post(user_id):
    user = User.query.get_or_404(user_id)

    title = request.form['title']
    content = request.form['content']
    tag_ids = request.form.getlist('tags')

    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    new_post = Post(title=title, content=content, user_id=user_id, tags=tags)

    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>', methods=['GET'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_details.html", post=post)

@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def show_edit_post_page(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("edit_post.html", post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    tag_ids = request.form.getlist('tags')
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.commit()
    return redirect(f'/posts/{post_id}')

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect('/users')

@app.route('/tags', methods=['GET'])
def show_tags_list():
    tags = Tag.query.all()
    return render_template('tags_list.html', tags=tags)


@app.route('/tags/<int:tag_id>', methods=['GET'])
def show_tag_details(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('show_tag.html', tag=tag)

@app.route('/tags/new', methods=['GET'])
def show_add_tag_form():
    return render_template('add_tag.html')

@app.route('/tags/new', methods=['POST'])
def add_new_tag():
    new_tag = Tag(name=request.form['tagName'])
    db.session.add(new_tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit', methods=['GET'])
def show_edit_tag_form(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('edit_tag.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def edit_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['tagName']
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    if tag:
        db.session.delete(tag)
        db.session.commit()
    return redirect('/tags')








