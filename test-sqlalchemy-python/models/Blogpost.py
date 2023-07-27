import sqlite3
from db import db

class Blogpost(db.Model):
    __tablename__ = 'Blogpost'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __init__(self,id,title,subtitle,author,content):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.content = content

    post = Blogpost(title=title , subtitle = subtitle, author = author)
    db.session.add(post)
    db.session.commit()