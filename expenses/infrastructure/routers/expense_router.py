from flask import Blueprint
from expenses.infrastructure.controllers.create_expense_controller import create_expense_blueprint
from expenses.infrastructure.controllers.list_expenses_controller import list_expenses_blueprint
from expenses.infrastructure.controllers.get_expense_controller import get_expense_blueprint

expense_router = Blueprint('expense_router', __name__)
expense_router.register_blueprint(create_expense_blueprint, url_prefix='/api/expenses')
expense_router.register_blueprint(list_expenses_blueprint, url_prefix='/api/expenses')
expense_router.register_blueprint(get_expense_blueprint, url_prefix='/api/expenses')
