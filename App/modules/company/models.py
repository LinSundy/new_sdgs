from App.ext import db


class Industry(db.Model):
    # 行业类别
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    companies = db.relationship('Company', backref='industry')


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)  # 公司名称
    info = db.Column(db.Text(256))  # 单位简介
    credentials = db.Column(db.String(2000))  # 资质情况
    register_capital = db.Column(db.String(20))  # 注册资金
    industry_type = db.Column(db.Integer, db.ForeignKey(Industry.id))  # 行业类别
    records = db.relationship('Records', backref='company')  # 已合作项目
    contact_person = db.Column(db.String(128))  # 联系人
    contacts = db.Column(db.String(128))  # 联系方式
    contacts1 = db.Column(db.String(128))  # 联系方式2
    recent_situation = db.Column(db.Text(256))  # 近三年情况
    url = db.Column(db.String(1000))  # 公司网址
    level = db.Column(db.Integer)  # 评级


class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey(Company.id))
    content = db.Column(db.Text(256))


