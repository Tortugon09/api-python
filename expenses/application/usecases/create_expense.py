from expenses.domain.entities.expense import Expense
from expenses.infrastructure.repositories.expense_repository import MongoDBExpenseRepository

class CreateExpense:
    def __init__(self, expense_repository: MongoDBExpenseRepository):
        self.expense_repository = expense_repository

    def execute(self, user_id, establishment, amount, priority):
        expense = Expense(establishment, amount, priority)
        return self.expense_repository.save(user_id, expense)
