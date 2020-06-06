from app.admin.common_view import CommonView
from flask import render_template
from .forms import CategoryForm
from app.services import category_srv


class CategoryView(CommonView):
    def __init__(self, *args):
        super().__init__(*args);
        self.form = CategoryForm()

    def get(self):
        top_category_list = category_srv.get_all()
        return render_template("admin/category.html", form=self.form, top_category_list=top_category_list)

    def post(self):
        return 'xxx'
