"""视图处理文件"""
import datetime
from re import match

import requests
from app import db
from app.models import ToDo
from flask import flash, render_template, request
from flask.helpers import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

from . import home  # 调用蓝图

@home.route("/test", methods=['GET'])
def test():
    return render_template('home/test.html')


@home.route("/", methods=['GET', 'POST'])
def index():
    # 一句话
    url = 'https://api.mcloc.cn/love'
    love_word = requests.get(url=url)

    # 时间计算
    starttime = datetime.datetime(2020, 10, 7, 17, 00, 00)
    now = datetime.datetime.now()
    interval = str((now-starttime).days)

    return render_template('home/index.html', word=love_word.text, interval=interval)


@home.route("/todo", methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        body = request.form.get('body')
        if not body or len(body) > 50:
            flash('无效输入')
            return redirect(url_for('home.todo'))
        todo = ToDo(body=body)
        db.session.add(todo)
        db.session.commit()
        flash('保存成功')
        return redirect(url_for('home.todo'))

    todos = ToDo.query.all()  # 查询表中所有事项
    todo_true = ToDo.query.filter_by(done=True).all()
    todo_false = ToDo.query.filter_by(done=False).all()
    return render_template('home/todo.html', todos=todos, todo_true=todo_true, todo_false=todo_false)


# 勾选选框事件
@home.route("/todo/check/<int:todo_id>", methods=["GET", "POST"])
def check(todo_id):
    todo_check = ToDo.query.get_or_404(todo_id)

    if request.method == 'POST':
        check = request.form['todo_1']
        if 'on' in check:
            todo_check.done = True
        else:
            todo_check.done = False

    db.session.commit()
    flash('更新成功')
    return redirect(url_for('home.todo'))


# 编辑
@home.route("/todo/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    todo = ToDo.query.get_or_404(todo_id)

    if request.method == 'POST':
        body = request.form['body']

        if not body or len(body) > 50:
            flash('无效输入')
            return redirect(url_for('home.edit', todo_id=todo_id))
        todo.body = body
        db.session.commit()
        flash('更新成功')
        return redirect(url_for('home.todo'))
    return render_template('home/edit.html', todo=todo)


# 删除
@home.route("/todo/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo = ToDo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('home.todo'))
