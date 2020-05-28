import click
from flask.cli import with_appcontext


@click.command()
@with_appcontext
def create_admin():
    """
    创建系统用户
    """

    from app.functions import is_email
    from app.services import admin_srv

    email = input('请输入邮箱:')

    while not is_email(email) or admin_srv.get_by_email(email):
        email = input('该邮箱格式错误或者已经存在,请重新输入:')

    password = input("请输入密码")
    while len(password) < 5:
        password = input('密码长度不能小于5个字符,请重新输入:')

    username = input("请输入用户名")

    data = {
        "email": email,
        "password": password,
        "username": username
    }
    admin_id = admin_srv.save(**data)

    if admin_id:
        print("成功管理员账号生成")
    else:
        print("管理员账号生成失败")
