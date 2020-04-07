from App.modules import db


class SysUser(db.Model):
    __tablename__ = 'sys_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(256), nullable=False)
