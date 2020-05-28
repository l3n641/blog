from .common import CommonService
from app.extensions import db


class AdminService(CommonService):

    def get_by_email(self, email):
        data = self.get_first(where={"email": email})
        return data

    def save(self, **kwargs):
        """注册新用户"""

        self.columns.append("password")
        user_id = CommonService.save(self, **kwargs)
        db.session.commit()
        return user_id
