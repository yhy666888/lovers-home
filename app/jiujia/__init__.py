from flask import Blueprint

jiujia = Blueprint("jiujia", __name__)  # 定义蓝图
import app.jiujia.views
