from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from bank_account.domain.entities.bank_account import BankAccount

class MongoDBBankAccountRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['users']

    def save_bank_account(self, user_email, bank_account: BankAccount):
        account_data = {
            'bank_account': {
                'name': bank_account.name,
                'account_number': bank_account.account_number,
                'expiry_date': bank_account.expiry_date.isoformat(),
                'nip': bank_account.nip
            }
        }
        self.collection.update_one({'email': user_email}, {'$set': account_data})
    
    def find_bank_account_by_user_id(self, user_id):
        user_data = self.collection.find_one({'_id': ObjectId(user_id)})
        if user_data and 'bank_account' in user_data:
            account_info = user_data['bank_account']
            # Asegúrate de incluir la parte de los milisegundos en el formato de fecha
            expiry_date = datetime.strptime(account_info['expiry_date'], "%Y-%m-%dT%H:%M:%S.%f")
            return BankAccount(
                name=account_info['name'],
                account_number=account_info['account_number'],
                expiry_date=expiry_date,
                nip=account_info['nip']
            )
        return None
    
    def update_nip(self, user_id, new_nip):
        result = self.collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': {'bank_account.nip': new_nip}}
        )
        return result.modified_count > 0  

    def delete_bank_account(self, user_id):
        result = self.collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$unset': {'bank_account': ""}}
        )
        return result.modified_count > 0  

