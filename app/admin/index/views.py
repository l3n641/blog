from flask.views import MethodView
from flask import render_template, session
from app.services import admin_srv


class IndexView(MethodView):
    def get(self):
        return render_template("admin/index.html")


class ProfileView(MethodView):
    def get(self):
        admin = admin_srv.get(session['admin_id'])
        return render_template('admin/profile.html', admin=admin)
