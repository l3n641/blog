from flask_ckeditor import CKEditorField
from wtforms import StringField, ValidationError
from wtforms.validators import Length, InputRequired
from flask_wtf import FlaskForm


class TagForm(FlaskForm):
    tag = StringField(validators=[InputRequired(message='请输入tag标签')])

    def validate_tag(self, field):
        from app.services import tag_srv
        tag = field.data
        if tag_srv.get_first({"name": tag}):
            raise ValidationError('该tag 已经存在')
