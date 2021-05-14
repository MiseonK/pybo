from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

# 첫 실행 세팅
# set FLASK_APP=pybo
# set FLASK_ENV=development

# 1. 패키지 생성
# 2. views 파일 생성
# 3. views에 py파일 생성할때 이름은 주로 주소를 따라간다 ex)webtoon_views.py
# 4. 뷰py에서 Blueprint를 생성하고 메인py에서 등록하고 실행

# 데이터베이스 연결(flask-migrate 패키지 설정)
# 1. config.py 생성 db정보 입력
# 2. __init__.py db,migrate설정
# 3. 터미널창에서 flask db init -> migrations 폴더 생성

# flask-migrate 패키지 생성
# 1. config.py생성   db정보입력
# 2. __init__.py db,migrate 설정
# 3. 터미널창에서 flask db init   -> migrations 폴더 생성
# 4. models.py 테이블구조 생성
# 5. flask db migrate -> 변경사항을 확인
# 6. flask db upgrade -> 즉시 적용하기 위한 명령어


db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)

    # migrate.init_app(app,db) 밑에 생성해야한다!
    from . import models

    from .views import main_views,naver_views,question_views,auth_views,answer_views,naver_views,movie_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(naver_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(naver_views.bp)
    app.register_blueprint(movie_views.bp)

    from .filter import format_datetime
    app.jinja_env.filters['datetime']=format_datetime

    return app









