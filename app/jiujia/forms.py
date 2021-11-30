from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class JiujiaForm(FlaskForm):
    date = StringField('年月', validators=[DataRequired(), Length(1, 10)])
    submit = SubmitField('查询')
