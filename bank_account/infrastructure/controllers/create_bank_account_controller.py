from flask import Blueprint, request, jsonify
from bank_account.application.usecases.create_bank_account import CreateBankAccount
from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository
from bank_account.infrastructure.services.bank_account_services import BankAccountServices

create_bank_account_blueprint = Blueprint('create_bank_account', __name__)

@create_bank_account_blueprint.route('/create', methods=['POST'])
def create_bank_account():
    data = request.get_json()
    if not data or not all(key in data for key in ['user_email', 'name']):
        return jsonify({"error": "User email and name are required"}), 400

    user_email = data['user_email']
    name = data['name']
    repository = MongoDBBankAccountRepository('mongodb://localhost:27017/', 'fync')
    services = BankAccountServices()
    use_case = CreateBankAccount(repository, services)

    try:
        use_case.execute(user_email, name)
        return jsonify({"message": "Bank account created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
