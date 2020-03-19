from app.extensions import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    modified_time = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    delete_time = db.Column(db.DateTime, nullable=True)


class Fingerprint(Base):
    hash = db.Column(db.String(120), unique=False, nullable=False, comment="简单的hash")
    info = db.Column(db.Text, nullable=False, comment="指纹具体参数")


class UserInfo(Base):
    Fingerprint_id = db.Column(db.Integer, unique=False, nullable=False, comment="指纹id")
    content = db.Column(db.Text, nullable=False, comment="设备对应的用户信息")

