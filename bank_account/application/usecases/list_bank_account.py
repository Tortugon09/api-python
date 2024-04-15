from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository

class ListBankAccount:
    def __init__(self, bank_account_repository: MongoDBBankAccountRepository):
        self.bank_account_repository = bank_account_repository

    def execute(self, user_id):
        return self.bank_account_repository.find_bank_account_by_user_id(user_id)

