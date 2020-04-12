from App.ext import db


class Industry(db.Model):
    # 行业类别
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    companies = db.relationship('Company', backref='industry')


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    info = db.Column(db.Text(256))
    register_capital = db.Column(db.String(20))
    industry_type = db.Column(db.Integer, db.ForeignKey(Industry.id))  # 行业类别
    records = db.relationship('Records', backref='company')  # 已合作项目
    contact_person = db.Column(db.String(128))  # 联系人
    contacts = db.Column(db.String(128))  # 联系方式
    recent_situation = db.Column(db.Text(256))  # 近三年情况
    url = db.Column(db.String(128))  # 公司网址


class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey(Company.id))
    content = db.Column(db.Text(256))


