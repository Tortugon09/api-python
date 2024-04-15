from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository

class DeleteBankAccount:
    def __init__(self, bank_account_repository: MongoDBBankAccountRepository):
        self.bank_account_repository = bank_account_repository

    def execute(self, user_id):
        return self.bank_account_repository.delete_bank_account(user_id)
