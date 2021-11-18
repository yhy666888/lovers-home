from flask import Blueprint

message = Blueprint("message", __name__)  # 定义蓝图
import app.message.views
