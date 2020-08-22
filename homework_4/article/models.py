from libs.orm import db


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime)
