import re
import json

class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0.0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance
        }

class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None): 
        if url == '/users':
            if payload:
                data = json.loads(payload)
                username = data['users']

                json_data = json.dumps(self.database)
                data = json.loads(json_data)
                for user in data['users']:
                    for name in username:
                        if user['name'] == name:
                            output = {'users': [user]}
                            user_formatted = str(output).replace("'",'"')
                            if len(username) == 1:
                                return user_formatted
            else:
                database_formatted = str(self.database).replace("'",'"')
                return database_formatted

    def post(self, url, payload=None):

        if url == '/add':
            data = json.loads(payload)
            name = data['user']            
            new_entry = User(name).to_dict()
            
            self.database["users"].append(new_entry)
            return str(new_entry).replace("'",'"')

        if url == '/iou':
            payload_data = json.loads(payload)
            lender = payload_data['lender']
            borrower = payload_data['borrower']
            amount = payload_data['amount']
            
            json_database = json.dumps(self.database)
            data = json.loads(json_database)
            for user in data['users']:
                owes_flag = False
                new_amount = amount
                if user['name'] == lender:
                    if borrower in user['owes']:
                        user['owes'][borrower] -= new_amount
                        if user['owes'][borrower] > 0:
                            owes_flag = True
                        elif user['owes'][borrower] == 0:
                            owes_flag = True
                            user['owes'].pop(borrower,None)
                        elif user['owes'][borrower] < 0:
                            new_amount = -user['owes'][borrower]
                            user['owes'].pop(borrower,None)
                    if owes_flag == False:
                        user['owed_by'].update({borrower: new_amount})
                    user['balance'] += amount
                if user['name'] == borrower:
                    if lender in user['owed_by']:
                        user['owed_by'][lender] -= new_amount
                        if user['owed_by'][lender] > 0:
                            owes_flag = True
                        elif user['owed_by'][lender] == 0:
                            owes_flag = True
                            user['owed_by'].pop(lender,None)
                        elif user['owed_by'][lender] < 0:
                            new_amount = -user['owed_by'][lender]
                            user['owed_by'].pop(lender,None)
                    if owes_flag == False:
                        user['owes'].update({lender: new_amount})
                    user['balance'] -= amount
            json_data = json.dumps(data)
            self.database = json.loads(json_data)

            database_dict = json.loads(json.dumps(self.database))
            results = {'users': []}
            for user in database_dict["users"]:
                if user["name"] == lender or user["name"] == borrower:
                    results["users"].append(user)

            database_formatted = str(results).replace("'",'"')
            
            return database_formatted
