from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.movieapi import Mrank
from ..forms import NaverBookForm

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')