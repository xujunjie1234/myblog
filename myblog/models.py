
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from myblog.extensions import db, whooshee


class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(20))
    blog_title = db.Column(db.String(30))
    name = db.Column(db.String(20))


    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)

@whooshee.register_model('name')
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    posts = db.relationship("Post",back_populates="category")

    def delete(self):
        default_category = Category.query.get(1)
        posts = self.posts[:]
        for post in posts:
            post.category = default_category
        db.session.delete(self)
        db.session.commit()

@whooshee.register_model('title','body')
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
    can_comment = db.Column(db.Boolean,default=True)
    read = db.Column(db.Integer)
    #likes = db.Column(db.Integer)

    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',back_populates='posts')

    comments = db.relationship('Comment',back_populates='post',cascade='all,delete-orphan')


class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    body = db.Column(db.Text)
    reviewed = db.Column(db.Boolean,default=False)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)

    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    post = db.relationship('Post',back_populates='comments')

    replies = db.relationship('Comment',back_populates='replied',cascade='all,delete-orphan') #子评论

    replied_id = db.Column(db.Integer,db.ForeignKey('comment.id'))
    replied = db.relationship('Comment',back_populates='replies',remote_side=[id]) 
