from bank_account.domain.entities.bank_account import BankAccount
from bank_account.infrastructure.repositories.bank_account_repository import MongoDBBankAccountRepository
from bank_account.infrastructure.services.bank_account_services import BankAccountServices
from bank_account.domain.validations.bank_account_validations import validate_account_number, validate_nip

class CreateBankAccount:
    def __init__(self, bank_account_repository: MongoDBBankAccountRepository, bank_account_services: BankAccountServices):
        self.bank_account_repository = bank_account_repository
        self.bank_account_services = bank_account_services

    def execute(self, user_email, name):
        account_number = self.bank_account_services.generate_account_number()
        expiry_date = self.bank_account_services.calculate_expiry_date()
        nip = self.bank_account_services.generate_nip()

        if not validate_account_number(account_number) or not validate_nip(nip):
            raise ValueError("Generated bank account details are invalid")

        bank_account = BankAccount(name, account_number, expiry_date, nip)
        self.bank_account_repository.save_bank_account(user_email, bank_account)
