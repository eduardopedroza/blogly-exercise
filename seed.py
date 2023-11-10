from models import db, User, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()
Tag.query.delete()

user1 = User(first_name='Chris', last_name='Paul', image_url='https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQlEosxGhyOcR70a0En1NYSjh62qMzhhaNB17RNyl8i1C2GXH2RSrwljsHCi7Mtl8izM6goagoDaU8pmk0')
user2 = User(first_name='James', last_name='Hard', image_url='https://cdn.nba.com/headshots/nba/latest/1040x760/201935.png')

db.session.add(user1)
db.session.add(user2)

tag1 = Tag(name='Fun')
tag2 = Tag(name='Learning')
tag3 = Tag(name='Coding')

db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)

db.session.commit()

post1 = Post(title='First Post', content='This is the first post by Chris', user_id=user1.id, created_at='2023-04-01 10:00:00', tags=[tag1, tag2])
post2 = Post(title='Second Post', content='This is the first post by James', user_id=user2.id, created_at='2023-04-02 10:00:00', tags=[tag2, tag3])

db.session.add(post1)
db.session.add(post2)

db.session.commit()
