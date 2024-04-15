from expenses.infrastructure.repositories.expense_repository import MongoDBExpenseRepository

class GetExpense:
    def __init__(self, expense_repository: MongoDBExpenseRepository):
        self.expense_repository = expense_repository

    def execute(self, user_id, expense_id):
        return self.expense_repository.find_expense_by_id(user_id, expense_id)
