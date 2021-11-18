from flask import Blueprint

todo = Blueprint("todo", __name__)  # 定义蓝图
import app.todo.views
