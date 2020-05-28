from flask.views import MethodView
from app.extensions import db


class CommonView(MethodView):
    def __del__(self):
        db.session.commit()
