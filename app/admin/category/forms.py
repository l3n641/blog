from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, ValidationError
from wtforms.validators import InputRequired


class CategoryForm(FlaskForm):
    parent_id = SelectField("parent_id", default=0, coerce=int)
    name = StringField("name", validators=[InputRequired(message='请填写栏目名称')])

    def validate_parent_id(self, field):
        from app.services import category_srv
        parent_id = field.data
        parent_category = category_srv.get_first({"parent_id": 0, 'id': parent_id})
        if not parent_category:
            raise ValidationError("parent id invalidate")
