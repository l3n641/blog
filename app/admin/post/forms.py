from flask_ckeditor import CKEditorField
from wtforms import StringField
from wtforms.validators import Length, InputRequired
from flask_wtf import FlaskForm


class PostForm(FlaskForm):
    title = StringField(validators=[InputRequired(message='请输入标题')])
    content = CKEditorField('Body')
