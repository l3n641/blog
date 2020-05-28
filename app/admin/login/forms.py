from wtforms import StringField
from wtforms.validators import Length, InputRequired, regexp, Regexp, EqualTo 
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField(validators=[Length(5, 20, message='邮箱长度不正确'), InputRequired(message='请填写邮箱')])
    password = StringField(validators=[Length(5, 20, message='密码长度不对')])
