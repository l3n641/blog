from flask import Blueprint, render_template, jsonify, redirect, views, request, session, g
from .forms import LoginForm
from app.services import admin_srv


class LoginView(views.MethodView):

    def __init__(self):
        super().__init__();
        self.form = LoginForm()

    def get(self):
        return render_template('login.html', form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            admin = admin_srv.get_by_email(self.form.data.get('email'))
            if admin and admin.check_pwd(self.form.data.get('password')):
                response = {
                    "code": 200,
                    "message": "登陆成功"
                }
            else:
                response = {
                    "code": 400,
                    "message": "用户不存在或者密码错误"
                }


        else:

            response = {
                "code": 400,
                "message": [msg for key, msg in self.form.errors.items()][0]
            }

        return jsonify(response)
