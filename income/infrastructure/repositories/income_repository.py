from pymongo import MongoClient
from bson.objectid import ObjectId 

class MongoDBIncomeRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['users'] 

    def save(self, user_id, income):
        income_data = {
            'amount': income.amount,
            'reason': income.reason,
            'priority': income.priority
        }
        result = self.collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$push': {'incomes': income_data}}
        )
        return result.modified_count > 0

    def find_incomes_by_user_id(self, user_id):
        user_data = self.collection.find_one({'_id': ObjectId(user_id)}, {'incomes': 1, '_id': 0})
        return user_data.get('incomes', [])