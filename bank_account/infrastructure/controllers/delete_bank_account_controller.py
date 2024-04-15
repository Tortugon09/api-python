from flask import Blueprint, request, jsonify
from bank_account.application.usecases.delete_bank_account import DeleteBankAccount
from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository

delete_bank_account_blueprint = Blueprint('delete_bank_account', __name__)

@delete_bank_account_blueprint.route('/delete/<user_id>', methods=['DELETE'])
def delete_bank_account(user_id):
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    repository = MongoDBBankAccountRepository('mongodb://localhost:27017/', 'fync')
    use_case = DeleteBankAccount(repository)

    success = use_case.execute(user_id)
    if success:
        return jsonify({"message": "Bank account deleted successfully"}), 200
    else:
        return jsonify({"error": "Bank account not found or could not be deleted"}), 404
