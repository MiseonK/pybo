from flask import Blueprint,render_template,url_for
from werkzeug.utils import redirect

from pybo.models import Question,Answer,User
from datetime import datetime
from pybo import db


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/test')
def test():
    for i in range(100):
        q=Question(subject='테스트 데이터 [%03d]'%i, content='내용무',create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
