from flask import Blueprint, request, jsonify
from bank_account.application.usecases.edit_bank_account import EditBankAccountNIP
from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository

edit_bank_account_blueprint = Blueprint('edit_bank_account', __name__)

@edit_bank_account_blueprint.route('/edit/<user_id>', methods=['PUT'])
def edit_bank_account_nip(user_id):
    data = request.get_json()
    new_nip = data.get('nip')
    if not new_nip:
        return jsonify({"error": "NIP is required"}), 400

    repository = MongoDBBankAccountRepository('mongodb://localhost:27017/', 'fync')
    use_case = EditBankAccountNIP(repository)

    try:
        success = use_case.execute(user_id, new_nip)
        if success:
            return jsonify({"message": "NIP updated successfully"}), 200
        else:
            return jsonify({"error": "Update failed"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
