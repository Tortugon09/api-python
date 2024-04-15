from expenses.infrastructure.repositories.expense_repository import MongoDBExpenseRepository

class ListExpenses:
    def __init__(self, expense_repository: MongoDBExpenseRepository):
        self.expense_repository = expense_repository

    def execute(self, user_id):
        return self.expense_repository.find_expenses_by_user_id(user_id)
