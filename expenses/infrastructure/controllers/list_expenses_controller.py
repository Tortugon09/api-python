from flask import Blueprint, request, jsonify
from expenses.application.usecases.list_expenses import ListExpenses
from expenses.infrastructure.repositories.expense_repository import MongoDBExpenseRepository

list_expenses_blueprint = Blueprint('list_expenses', __name__)

@list_expenses_blueprint.route('/list/<user_id>', methods=['GET'])
def list_expenses(user_id):
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    repository = MongoDBExpenseRepository('mongodb://localhost:27017/', 'fync')
    use_case = ListExpenses(repository)

    expenses = use_case.execute(user_id)
    if expenses is not None:
        return jsonify({"expenses": expenses}), 200
    else:
        return jsonify({"error": "No expenses found for this user"}), 404
