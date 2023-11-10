
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)



class User(db.Model):
    """User"""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(20),
                           nullable=False)
    
    last_name = db.Column(db.String(20),
                           nullable=False)
    
    image_url = db.Column(db.String(50))
    
    posts = db.relationship('Post', 
                            backref='author')
    
class Post(db.Model):
    """Post"""
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.String(20),
                      nullable=False)
    
    content = db.Column(db.String(1000),
                        nullable=False)
    
    created_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp())

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'), 
                        nullable=False)
    
    tags = db.relationship('Tag',
                           secondary='post_tags',
                           backref='posts')
    
    post_tags = db.relationship('PostTag', backref='post')
    
class Tag(db.Model):
    """Tags"""

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(15),
                     nullable=False,
                     unique=True)
    
    tag_posts = db.relationship('PostTag', backref='tag')

    
class PostTag(db.Model):
    """PostTags"""

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True,
                        nullable=False)

    tag_id = db.Column(db.Integer,
                       db.ForeignKey('tags.id'),
                       primary_key=True,
                       nullable=False)