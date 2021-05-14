import os

BASE_DIR=os.path.dirname(__file__)  # 현재 폴더경로를 가져옴

# format(문구) -> {}에 들어갈 문구
# os.path.join(경로,데이터베이스) -> 경로에 있는 데이터베이스 사용
SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS=False

SECRET_KEY= "dev"