import demjson
from flask_restful import Resource, reqparse, marshal_with, fields
from .models import Company, Records
from ...ext import db
from ...utils import handle_data

parser = reqparse.RequestParser()
parser.add_argument('data', type=str, location='json')
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)
parser.add_argument('pageNum', type=int)
parser.add_argument('pageSize', type=int)


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
            contacts1 = company.get('contacts1')
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
                current_company.contacts = contacts
                current_company.contacts1 = contacts1
                current_company.recent_situation = recent_situation
                current_company.url = url
                current_company.level = level
                Records.query.filter(Records.company_id.__eq__(current_company.id)).delete()
                add_company_list.append(current_company)
            else:
                current_company = Company(name=name, info=info, register_capital=register_capital,
                                          industry_type=industry_type, contact_person=contact_person,
                                          contacts=contacts, contacts1=contacts1, recent_situation=recent_situation,
                                          url=url, level=level)
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
    paginate_fields = {
        'page': fields.Integer,
        'pages': fields.Integer,
        'total': fields.Integer,
        'has_prev': fields.Boolean,
        'has_next': fields.Boolean
    }

    data_fields = {
        'companies': fields.List(fields.Nested(company_fields)),
        'paginate': fields.Nested(paginate_fields)
    }

    json_fields = {
        'code': fields.Integer,
        'data': fields.Nested(data_fields),
        'msg': fields.String
    }

    @marshal_with(json_fields)
    def post(self):
        args = parser.parse_args()
        page_num = args.get('pageNum')
        page_size = args.get('pageSize')
        params_data = demjson.decode(args.get('data'))
        search_value = params_data.get('search_value') or None
            # company = Company.query.filter(Company.name.contains(search_value))
            # try:
        pagination = Company.query.paginate(page=page_num, per_page=page_size, error_out=False)
            # except Exception as e:
            #     pagination = Company.query.paginate(page=page_num-1, per_page=page_size)
        paginate_data = dict()
        paginate_data['page'] = pagination.page
        paginate_data['pages'] = pagination.pages
        paginate_data['total'] = pagination.total
        paginate_data['has_prev'] = pagination.has_prev
        paginate_data['has_next'] = pagination.has_next
        companies = pagination.items
        json_data = {
            'companies': companies,
            'paginate': paginate_data
        }
        return handle_data(json_data)

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


class RecordApi(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        name = args.get('name')
        company_id = args.get('id')
        record = Records(company_id=company_id, content=name)
        try:
            db.session.add(record)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return handle_data({'id': record.id, 'content': name, 'company_id': company_id})

    @staticmethod
    def delete():
        args = parser.parse_args()
        record_id = args.get('id')
        record = Records.query.get(record_id)
        try:
            db.session.delete(record)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return handle_data('删除数据成功!')

    @staticmethod
    def put():
        args = parser.parse_args()
        record_id = args.get('id')
        name = args.get('name')
        print(record_id, '我娃')
        record = Records.query.get(record_id)
        record.content = name
        try:
            db.session.add(record)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return handle_data({'id': record_id, 'content': name, 'company_id': record.id})


class AddOneCompany(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        company = demjson.decode(args.get('data'))
        print(company, '公司')
        name = company.get('name')
        industry_type = company.get('industry_type')
        info = company.get('info')
        register_capital = company.get('register_capital')
        contact_person = company.get('contact_person')
        contacts = company.get('contacts')
        contacts1 = company.get('contacts1')
        level = company.get('level')
        recent_situation = company.get('recent_situation')
        url = company.get('url')
        records = company.get('records')
        current_company = Company(name=name, info=info, register_capital=register_capital,
                                  industry_type=industry_type, contact_person=contact_person,
                                  contacts=contacts, contacts1=contacts1, recent_situation=recent_situation,
                                  url=url, level=level)
        db.session.add(current_company)
        db.session.flush()
        for record in records:
            current_record = Records(company_id=current_company.id, content=record.get('content'))
            db.session.add(current_record)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return handle_data('添加成功!')

    @staticmethod
    def put():
        args = parser.parse_args()
        data = args.get('data')
        company = demjson.decode(data)
        print(company, '参数')
        name = company.get('name')
        industry_type = company.get('industry_type')
        info = company.get('info')
        register_capital = company.get('register_capital')
        contact_person = company.get('contact_person')
        contacts = company.get('contacts')
        contacts1 = company.get('contacts1')
        level = company.get('level')
        recent_situation = company.get('recent_situation')
        url = company.get('url')
        company_id = company.get('id')
        current_company = Company.query.get(company_id)
        current_company.name = name
        current_company.industry_type = industry_type
        current_company.info = info
        current_company.register_capital = register_capital
        current_company.contact_person = contact_person
        current_company.contacts = contacts
        current_company.contacts1 = contacts1
        current_company.level = level
        current_company.recent_situation = recent_situation
        current_company.url = url
        try:
            db.session.add(current_company)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return handle_data('修改成功!')