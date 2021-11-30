from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)  # 实例化flask
app.debug = True  # 开启调试

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:yhy666888@127.0.0.1:3306/home"  # 定义数据库链接
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.secret_key = 'yzyzyzflask'

db = SQLAlchemy(app)  # 定义db对象，实例化SQLAlchemy
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from app.todo import todo as home_blueprint  # 导入
from app.message import message as message_blueprint
from app.user import user as user_blueprint
from app.jiujia import jiujia as jiujia_blueprint

app.register_blueprint(home_blueprint)  # 注册蓝图
app.register_blueprint(message_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(jiujia_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
