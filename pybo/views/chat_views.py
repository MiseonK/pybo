from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.movieapi import Mrank
from .dialogflowapi import chat
from ..forms import HelpForm

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')

@bp.route('/help/',methods=('GET','POST'))
def Help():
    form = HelpForm()
    if request.method == 'POST' and form.validate_on_submit():
        result=chat(form.search.data,'1234')
        if result == '영화순위메뉴':
            return redirect(url_for('movie.Movierank'))
        if result == '구글가자':
            return redirect(url_for('https://www.google.co.kr/'))
    return render_template('chat/help.html',form=form)