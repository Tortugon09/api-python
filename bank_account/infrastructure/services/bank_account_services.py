import random
from datetime import datetime, timedelta

class BankAccountServices:
    def generate_account_number(self):
        return "7490" + "".join([str(random.randint(0, 9)) for _ in range(12)])

    def generate_nip(self):
        return "".join([str(random.randint(0, 9)) for _ in range(4)])

    def calculate_expiry_date(self):
        return datetime.utcnow() + timedelta(days=180)  # Aproximadamente 6 meses
