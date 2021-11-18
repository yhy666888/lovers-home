from flask import flash, redirect, url_for, render_template
from app import db
from app.models import Message
from . import message
from .forms import MessageForm


@message.route('/message', methods=['GET', 'POST'])
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
