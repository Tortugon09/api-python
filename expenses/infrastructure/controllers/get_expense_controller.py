from flask import Blueprint, request, jsonify
from expenses.application.usecases.get_expense import GetExpense
from expenses.infrastructure.repositories.expense_repository import MongoDBExpenseRepository

get_expense_blueprint = Blueprint('get_expense', __name__)

@get_expense_blueprint.route('/get/<user_id>/<expense_id>', methods=['GET'])
def get_expense(user_id, expense_id):
    if not user_id or not expense_id:
        return jsonify({"error": "User ID and Expense ID are required"}), 400

    repository = MongoDBExpenseRepository('mongodb://localhost:27017/', 'fync')
    use_case = GetExpense(repository)

    expense = use_case.execute(user_id, expense_id)
    if expense:
        return jsonify({"expense": expense}), 200
    else:
        return jsonify({"error": "Expense not found"}), 404
