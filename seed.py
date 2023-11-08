from models import db, User, Post
from app import app

db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()

user1 = User(first_name='John', last_name='Doe', image_url='http://example.com/johndoe.jpg')
user2 = User(first_name='Jane', last_name='Doe', image_url='http://example.com/janedoe.jpg')

db.session.add(user1)
db.session.add(user2)

db.session.commit()

post1 = Post(title='First Post', content='This is the first post by John', user_id=user1.id, created_at='2023-04-01 10:00:00')
post2 = Post(title='Second Post', content='This is the first post by Jane', user_id=user2.id, created_at='2023-04-02 10:00:00')

db.session.add(post1)
db.session.add(post2)

db.session.commit()
