from pymongo import MongoClient
from bson.objectid import ObjectId  

class MongoDBExpenseRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['users']  

    def save(self, user_id, expense):
        expense_data = {
            'establishment': expense.establishment,
            'amount': expense.amount,
            'priority': expense.priority
        }

        result = self.collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$push': {'expenses': expense_data}}
        )
        return result.modified_count > 0 

    def find_expenses_by_user_id(self, user_id):
        user_data = self.collection.find_one({'_id': ObjectId(user_id)}, {'expenses': 1, '_id': 0})
        return user_data.get('expenses', [])

    def find_expense_by_id(self, user_id, expense_id):
        user_data = self.collection.find_one(
            {'_id': ObjectId(user_id), 'expenses._id': ObjectId(expense_id)},
            {'expenses.$': 1, '_id': 0}
        )
        if user_data and 'expenses' in user_data and len(user_data['expenses']) > 0:
            return user_data['expenses'][0]
        return None