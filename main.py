from flask import Flask, jsonify
from flask_cors import CORS
from user.infrastructure.routers.user_router import user_router
from bank_account.infrastructure.routers.bank_account_router import bank_account_router
from expenses.infrastructure.routers.expense_router import expense_router
from user.infrastructure.middleware.user_middleware import token_required
from income.infrastructure.routers.income_router import income_router

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
app.register_blueprint(user_router)
app.register_blueprint(bank_account_router)
app.register_blueprint(expense_router)
app.register_blueprint(income_router)

@app.route('/protected')
@token_required
def protected_route():
    return jsonify({"message": "This route is only accessible with a valid token."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')