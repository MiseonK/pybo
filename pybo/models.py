from pybo import db

# 설계도 같은 개념 Question-테이블 이름
# DB잘못 만들었을때-> 수정-> migrations, pybo.db 삭제하고 다시 생성
class Question(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    subject=db.Column(db.String(200),nullable=False)
    content=db.Column(db.Text(),nullable=False)
    create_date=db.Column(db.DateTime(),nullable=False)

class Answer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    question_id=db.Column(db.Integer,db.ForeignKey('question.id',ondelete='CASCADE'))
    question=db.relationship('Question',backref=db.backref('answer_set')) #answer_set으로 자동으로 데이터 들어감
    content=db.Column(db.Text(),nullable=False)
    create_date=db.Column(db.DateTime,nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150),unique=True,nullable=False)  #유니크:같은값 저장x
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)