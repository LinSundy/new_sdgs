from flask import Blueprint
from flask_restful import Api

from .apis import CompanyApi

company = Blueprint('company', __name__)

api = Api(company)

api.add_resource(CompanyApi, '/company')
