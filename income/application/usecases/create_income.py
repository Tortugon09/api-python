from income.domain.entities.income import Income
from income.infrastructure.repositories.income_repository import MongoDBIncomeRepository

class CreateIncome:
    def __init__(self, income_repository: MongoDBIncomeRepository):
        self.income_repository = income_repository

    def execute(self, user_id, amount, reason, priority):
        income = Income(amount, reason, priority)
        return self.income_repository.save(user_id, income)
