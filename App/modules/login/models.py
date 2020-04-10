from App.ext import db


class SysUser(db.Model):
    __tablename__ = 'sys_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(256), nullable=False)
    roles = db.relationship('Role', backref='user')
    avatar = db.Column(db.String(256), default='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif')
    name = db.Column(db.String(128), default='')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('sys_user.id'))
