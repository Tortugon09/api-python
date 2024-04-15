from datetime import datetime

class BankAccount:
    def __init__(self, name, account_number, expiry_date, nip):
        self.name = name
        self.account_number = account_number
        self.expiry_date = expiry_date
        self.nip = nip
