"""数据模型文件"""
from app import db
import datetime


# 定义用户模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(256))  # 密码
    sex = db.Column(db.String(255), unique=True)  # 性别
    face = db.Column(db.String(255), unique=True)  # 头像
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 添加时间
    userlogs = db.relationship('UserLog', backref='user')  # 会员日志外键关系关联，backref互相绑定user表码
    messages = db.relationship('Message', back_populates='author', cascade='all')
    todo = db.relationship('ToDo', back_populates='author', cascade='all', )

    def __repr__(self):
        return "<User %r>" % self.name
          
    def check_pwd(self, pwd):
        """验证密码是否正确，直接将hash密码和输入的密码进行比较，如果相同则返回True"""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 用户日志
class UserLog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    ip = db.Column(db.String(100))  # 登录IP
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id


# 待办事项
class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='todo')


# 消息
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='messages')


# if __name__ == '__main__':
#     # db.create_all()  # 创建数据表
#     # 添加用户
#     from werkzeug.security import generate_password_hash
#     user = User(
#         name='test',
#         pwd=generate_password_hash('password'),
#         sex='男'
#     )
#     db.session.add(user)
#     db.session.commit()
