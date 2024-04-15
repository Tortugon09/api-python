from income.infrastructure.repositories.income_repository import MongoDBIncomeRepository

class ListIncomes:
    def __init__(self, income_repository: MongoDBIncomeRepository):
        self.income_repository = income_repository

    def execute(self, user_id):
        return self.income_repository.find_incomes_by_user_id(user_id)
