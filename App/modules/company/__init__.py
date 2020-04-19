from flask import Blueprint
from flask_restful import Api

from .apis import CompanyApi, CompanySearchApi, RecordApi, AddOneCompany, IndustryApi

company = Blueprint('company', __name__)

api = Api(company)

api.add_resource(CompanyApi, '/company/list/')
api.add_resource(CompanySearchApi, '/companies/')
api.add_resource(RecordApi, '/record/')
api.add_resource(AddOneCompany, '/oneCompany/')
api.add_resource(IndustryApi, '/industry/')
