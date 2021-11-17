from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)  # 实例化flask
app.debug = True  # 开启调试

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:yhy666888@127.0.0.1:3306/home"  # 定义数据库链接
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'yzyzyzflask'

db = SQLAlchemy(app)  # 定义db对象，实例化SQLAlchemy
migrate = Migrate(app, db)

from app.home import home as home_blueprint  # 导入

app.register_blueprint(home_blueprint)  # 注册蓝图

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404