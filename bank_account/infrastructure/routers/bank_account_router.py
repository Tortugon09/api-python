from flask import Blueprint
from bank_account.infrastructure.controllers.create_bank_account_controller import create_bank_account_blueprint
from bank_account.infrastructure.controllers.list_bank_account_controller import list_bank_account_blueprint
from bank_account.infrastructure.controllers.edit_bank_account_controller import edit_bank_account_blueprint
from bank_account.infrastructure.controllers.delete_bank_account_controller import delete_bank_account_blueprint

bank_account_router = Blueprint('bank_account_router', __name__)
bank_account_router.register_blueprint(create_bank_account_blueprint, url_prefix='/api/bank_accounts')
bank_account_router.register_blueprint(list_bank_account_blueprint, url_prefix='/api/bank_accounts')
bank_account_router.register_blueprint(edit_bank_account_blueprint, url_prefix='/api/bank_accounts')
bank_account_router.register_blueprint(delete_bank_account_blueprint, url_prefix='/api/bank_accounts')
