import demjson
from flask_restful import Resource, reqparse, marshal_with, fields
from .models import Company, Records
from ...ext import db
from ...utils import handle_data

parser = reqparse.RequestParser()
parser.add_argument('data', type=str, location='json')
parser.add_argument('id', type=int)


class CompanyApi(Resource):
    @staticmethod
    def get():
        args = parser.parse_args()
        company_id = args.get('id')
        return handle_data('ok')

    @staticmethod
    def post():
        data = parser.parse_args()
        add_companies = data.get('data')
        company_list = []
        add_company_list = []
        for index, company in enumerate(demjson.decode(add_companies)):
            name = company.get('name')
            industry_type = company.get('industry_type')
            info = company.get('info')
            register_capital = company.get('register_capital')
            contact_person = company.get('contact_person')
            contacts = company.get('contacts')
            level = company.get('level')
            recent_situation = company.get('recent_situation')
            url = company.get('url')
            records = company.get('records')
            current_company = Company.query.filter(Company.name.__eq__(name)).first()
            if current_company:
                current_company.industry_type = industry_type
                current_company.info = info
                current_company.register_capital = register_capital
                current_company.contact_person = contact_person
                phones = contacts.split(',')
                current_company.contacts = phones[0]
                current_company.contacts1 = phones[1] if len(phones) > 1 else None
                current_company.recent_situation = recent_situation
                current_company.url = url
                current_company.level = level
                Records.query.filter(Records.company_id.__eq__(current_company.id)).delete()
                add_company_list.append(current_company)
            else:
                current_company = Company(name=name, info=info, register_capital=register_capital,
                                          industry_type=industry_type, contact_person=contact_person,
                                          contacts=contacts, recent_situation=recent_situation, url=url, level=level)
                company_list.append(current_company)
            db.session.add(current_company)
            db.session.flush()
            for record in records.split(','):
                current_record = Records(company_id=current_company.id, content=record)
                db.session.add(current_record)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
            nums = {
                'update': len(add_company_list),
                'add': len(company_list)
            }
        return handle_data(nums)


class CompanySearchApi(Resource):
    record_fields = {
        'id': fields.Integer,
        'content': fields.String,
        'company_id': fields.Integer
    }
    company_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'info': fields.String,
        'register_capital': fields.String,
        'industry_type': fields.Integer,
        'records': fields.Nested(record_fields),
        'contact_person': fields.String,
        'contacts': fields.String,
        'contacts1': fields.String,
        'recent_situation': fields.String,
        'url': fields.String,
        'level': fields.String
    }
    data = {
        'code': fields.Integer,
        'data': fields.List(fields.Nested(company_fields)),
        'msg': fields.String
    }

    @marshal_with(data)
    def get(self):
        companies = Company.query.all()
        return handle_data(companies)

    @staticmethod
    def delete():
        args = parser.parse_args()
        company_id = args.get('id')
        try:
            company = Company.query.get(company_id)
            db.session.delete(company)
            db.session.query(Records).filter(Records.company_id.__eq__(company_id)).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return handle_data('success')
