import datetime

from flask import Blueprint
from flask import request
from flask import redirect
from flask import render_template

from libs.orm import db
from article.models import Article

article_bp = Blueprint('article', __name__, url_prefix='/article')
article_bp.template_folder = './templates'


@article_bp.route('/index')
def index():
    articles = Article.query.order_by(Article.created.desc()).all()
    return render_template('index.html', articles=articles)


@article_bp.route('/post', methods=("POST", "GET"))
def post_article():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        now = datetime.datetime.now()

        article = Article(title=title, content=content, created=now)
        db.session.add(article)
        db.session.commit()
        return redirect('/article/read?aid=%s' % article.id)
    else:
        return render_template('post.html')


@article_bp.route('/read')
def read_article():
    aid = int(request.args.get('aid'))
    article = Article.query.get(aid)
    return render_template('read.html', article=article)


@article_bp.route('/delete')
def delete_article():
    aid = int(request.args.get('aid'))
    Article.query.filter_by(id=aid).delete()
    db.session.commit()
    return redirect('/article/index')
