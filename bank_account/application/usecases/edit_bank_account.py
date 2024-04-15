from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository
from bank_account.domain.validations.bank_account_validations import validate_nip

class EditBankAccountNIP:
    def __init__(self, bank_account_repository: MongoDBBankAccountRepository):
        self.bank_account_repository = bank_account_repository

    def execute(self, user_id, new_nip):
        if not validate_nip(new_nip):
            raise ValueError("Invalid NIP format")

        return self.bank_account_repository.update_nip(user_id, new_nip)
