from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question

bp = Blueprint('question',__name__,url_prefix='/question')

@bp.route('/list/')
def _list():
    page=request.args.get('page',type=int,default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list=question_list.paginate(page,per_page=10)
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form=AnswerForm()

    question = Question.query.get_or_404(question_id)
    return render_template('question/detail.html',question=question,form=form)

@bp.route('/create/',methods=('GET','POST'))
def create():
    form = QuestionForm()
    if request.method=='POST' and form.validate_on_submit():
        question=Question(subject=form.subject.data, content=form.content.data,create_date=datetime.now)
        db.session.add(question)
        db.session.commit()
        return render_template('question/question_form.html',form=form)
    return redirect(url_for('main.index'))













