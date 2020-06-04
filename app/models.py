from app.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    modified_time = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    delete_time = db.Column(db.DateTime, nullable=True)


class Admin(Base):
    __tablename__ = 'admin'

    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    @property
    def password(self):
        raise ("密码无法读取")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_pwd(self, raw_password):
        result = check_password_hash(self.password_hash, raw_password)
        return result


class Post(Base):
    __tablename__ = 'post'

    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    author = db.relationship("Admin", backref='post')
    post_views=db.relationship("PostViews",uselist=False, backref="post")


post_tag = db.Table(
    'post_tag',
    db.Column('post_id', db.ForeignKey("post.id"), primary_key=True),
    db.Column('tag_id', db.ForeignKey("tag.id"), primary_key=True)
)


class Tag(Base):
    __tablename__ = 'tag'

    name = db.Column(db.String(150))
    post = db.relationship("Post", backref='tags', secondary=post_tag)


class PostViews(db.Model):
    __tablename__ = "post_views"

    amount = db.Column(db.Integer, nullable=False, server_default="0")
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), primary_key=True)

