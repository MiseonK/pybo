from flask import Blueprint,render_template,url_for,request
from werkzeug.utils import redirect
from ..forms import NaverBookForm,NaverMovieForm
from pybo.naverapi import naverbook,navermovie

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/book', methods=['GET', 'POST'])
def Naverbook():
    form=NaverBookForm()  # 검색어에 내용이 있을 경우
    if request.method == 'POST' and form.validate_on_submit():
        result = naverbook(form.search.data)
        return render_template('naver/naverbook.html',bookinfo_list=result['items'],form=form)
    return render_template('naver/naverbook.html',form=form)


class NavermovieForm(object):
    pass


@bp.route('/movie', methods=['GET', 'POST'])
def Navermovie():
    form=NaverMovieForm()  # 검색어에 내용이 있을 경우
    if request.method == 'POST' and form.validate_on_submit():
        result = navermovie(form.search.data)
        return render_template('naver/navermovie.html',movieinfo_list=result['items'],form=form)
    return render_template('naver/navermovie.html',form=form)