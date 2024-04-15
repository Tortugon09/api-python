from flask import Blueprint, request, jsonify
from income.application.usecases.create_income import CreateIncome
from income.infrastructure.repositories.income_repository import MongoDBIncomeRepository

create_income_blueprint = Blueprint('create_income', __name__)

@create_income_blueprint.route('/create/<user_id>', methods=['POST'])
def create_income(user_id):
    data = request.get_json()
    if not data or not all(key in data for key in ['amount', 'reason', 'priority']):
        return jsonify({"error": "All fields (amount, reason, priority) are required"}), 400

    repository = MongoDBIncomeRepository('mongodb://localhost:27017/', 'fync')
    use_case = CreateIncome(repository)

    if use_case.execute(user_id, data['amount'], data['reason'], data['priority']):
        return jsonify({"message": "Income added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add income"}), 400
