from flask import Blueprint
from income.infrastructure.controllers.create_income_controller import create_income_blueprint
from income.infrastructure.controllers.list_incomes_controller import list_incomes_blueprint

income_router = Blueprint('income_router', __name__)
income_router.register_blueprint(create_income_blueprint, url_prefix='/api/income')
income_router.register_blueprint(list_incomes_blueprint, url_prefix='/api/income')