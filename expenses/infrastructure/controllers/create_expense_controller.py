from flask import Blueprint, request, jsonify
from expenses.application.usecases.create_expense import CreateExpense
from expenses.infrastructure.repositories.expense_repository import MongoDBExpenseRepository

create_expense_blueprint = Blueprint('create_expense', __name__)

@create_expense_blueprint.route('/create/<user_id>', methods=['POST'])
def create_expense(user_id):
    data = request.get_json()
    if not data or not all(key in data for key in ['establishment', 'amount', 'priority']):
        return jsonify({"error": "All fields (establishment, amount, priority) are required"}), 400

    repository = MongoDBExpenseRepository('mongodb://localhost:27017/', 'fync')
    use_case = CreateExpense(repository)

    if use_case.execute(user_id, data['establishment'], data['amount'], data['priority']):
        return jsonify({"message": "Expense added successfully to user"}), 201
    else:
        return jsonify({"error": "Failed to add expense"}), 400
