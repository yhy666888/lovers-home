from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    """会员登录表单"""
    name = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号！')
        ],
        # description='账号',
        render_kw={
            'placeholder': "请输入账号",
            'required': "required"
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码！')
        ],
        # description='密码',
        render_kw={
            'placeholder': "请输入密码",
            'required': "required",
            'autofocus': "autofocus"
        }
    )
    submit = SubmitField(
        label='登录',
    )