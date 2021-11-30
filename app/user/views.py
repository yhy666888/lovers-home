from flask import flash, redirect, url_for, render_template, request, session
from app import db
from app.models import User
from . import user
from .forms import LoginForm
from functools import wraps


# 需要登录才能访问
def user_login_require(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('login_user', None) is None:
        # 如果session中未找到该键，则用户需要登录
            return redirect(url_for('user.login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

@user.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data['name']).first()
        if user == None or not user.check_pwd(data['pwd']):
            flash('用户名或密码错误!', 'danger')
            return redirect(url_for('user.login'))
        session['login_user'] = user.name
        session['login_user_id'] = user.id
        flash('登录成功~', 'success')
        return redirect(url_for('todo.index'))
    return render_template('user/login.html', form=form)

@user.route('/logout/')
def logout():
    session.pop('login_user', None)
    session.pop('login_user_id', None)
    return redirect(url_for('user.login'))
