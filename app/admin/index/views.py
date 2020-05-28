from flask.views import MethodView
from flask import render_template, session, jsonify
from app.services import admin_srv
from .forms import ResetpwdForm
from app.admin.common_view import CommonView


class IndexView(CommonView):
    def get(self):
        return render_template("admin/index.html")


class ProfileView(CommonView):
    def get(self):
        admin = admin_srv.get(session['admin_id'])
        return render_template('admin/profile.html', admin=admin)


class RestPasswordView(CommonView):
    """
    admin 更新密码
    """

    def __init__(self):
        super().__init__()
        self.form = ResetpwdForm()

    def get(self):
        return render_template("admin/resetpwd.html", form=self.form)

    def post(self):
        admin = admin_srv.get(session["admin_id"])
        if not self.form.validate_on_submit():
            response = {
                "code": 400,
                "message": [msg for key, msg in self.form.errors.items()][0]
            }

        if admin.check_pwd(self.form.data.get("oldpwd")):

            admin.password = self.form.data.get("newpwd")

            response = {
                "code": 200,
                "message": "更新密码成功"
            }
        else:

            response = {
                "code": 400,
                "message": "旧密码错误"
            }

        return jsonify(response)
