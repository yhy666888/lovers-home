from flask import Blueprint

home = Blueprint("home", __name__)  # 定义蓝图
import app.home.views
