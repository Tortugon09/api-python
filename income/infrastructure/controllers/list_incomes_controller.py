from flask import Blueprint, request, jsonify
from income.application.usecases.list_incomes import ListIncomes
from income.infrastructure.repositories.income_repository import MongoDBIncomeRepository

list_incomes_blueprint = Blueprint('list_incomes', __name__)

@list_incomes_blueprint.route('/list/<user_id>', methods=['GET'])
def list_incomes(user_id):
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    repository = MongoDBIncomeRepository('mongodb://localhost:27017/', 'fync')
    use_case = ListIncomes(repository)

    incomes = use_case.execute(user_id)
    if incomes is not None:
        return jsonify({"incomes": incomes}), 200
    else:
        return jsonify({"error": "No incomes found for this user"}), 404
