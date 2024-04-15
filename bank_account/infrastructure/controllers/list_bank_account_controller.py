from flask import Blueprint, request, jsonify
from bank_account.application.usecases.list_bank_account import ListBankAccount
from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository

list_bank_account_blueprint = Blueprint('list_bank_account', __name__)

@list_bank_account_blueprint.route('/list/<user_id>', methods=['GET'])
def list_bank_account(user_id):
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    repository = MongoDBBankAccountRepository('mongodb://localhost:27017/', 'fync')
    use_case = ListBankAccount(repository)

    bank_account = use_case.execute(user_id)
    if bank_account:
        return jsonify({
            "name": bank_account.name,
            "account_number": bank_account.account_number,
            "expiry_date": bank_account.expiry_date.strftime("%Y-%m-%d"),
            "nip": bank_account.nip
        }), 200
    else:
        return jsonify({"error": "Bank account not found"}), 404