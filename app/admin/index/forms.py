from wtforms import StringField
from wtforms.validators import Length, InputRequired, EqualTo
from flask_wtf import FlaskForm


class ResetpwdForm(FlaskForm):
    oldpwd = StringField(validators=[InputRequired(message='请输旧新密码'), Length(6, 18, message='密码长度不正确')])
    newpwd = StringField(validators=[InputRequired(message='请输入新密码'), Length(6, 18, message='密码长度不正确')])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message='确认密码必须和新密码保持一致')])
