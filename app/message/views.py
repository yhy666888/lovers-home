from flask import flash, redirect, url_for, render_template, request
from app import db
from app.models import Message
from app.user.views import user_login_require
from . import message
from .forms import MessageForm


@message.route('/message', methods=['GET', 'POST'])
@user_login_require
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('留言成功~')
        return redirect(url_for('message.index'))
    return render_template('message/message.html', form=form, messages=messages)


@message.route('/message/delete/<int:delete_id>/', methods=['POST'])
@user_login_require
def delete(delete_id):
    message = Message.query.get_or_404(delete_id)
    db.session.delete(message)
    db.session.commit()
    flash('删除留言成功')
    return redirect(url_for('message.index'))


@message.route('/message/edit/<int:edit_id>/', methods=['GET', 'POST'])
@user_login_require
def edit(edit_id):
    message = Message.query.get_or_404(edit_id)
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        if not body or len(body) > 50:
            flash('无效输入')
            return redirect(url_for('message.index', message_id=edit_id))
        message.name = name
        message.body = body
        db.session.commit()
        flash('更新成功')
        return redirect(url_for('message.index'))
    return render_template('message/edit.html', message=message, form=form)
