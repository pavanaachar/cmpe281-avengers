from pymongo import MongoClient
import uuid
import os, base64

client = MongoClient('mongodb://localhost:27017/')

# book-store is the database name
db = client['book-store']

# Collections
user_data = db['Users']
sessions_data = db['Sessions']

class User:
    def __init__(self, first_name, last_name, email, password):
        self.id = generate_userid()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


def generate_session():
    return base64.b64encode(os.urandom(16))

def generate_userid():
    return str(uuid.uuid4())

def add_session(userID):
    sessionvalue = generate_session()
    result = sessions_data.insert_one(
        {
            'userID': userID,
            'sessionID': sessionvalue
        }
    )
    print('session id : ' + str(sessionvalue))
    print('result : ' + str(result.inserted_id))

def add_user(user):
    result = user_data.insert_one(
            {
                'ID': user.id,
                'First name': user.first_name,
                'Last name': user.last_name,
                'Email': user.email,
                'Password': user.password
            }
        )
    print('user id : ' + user.id)
    print('result : ' + str(result.inserted_id))


if __name__ == '__main__':
    new_user = User("Amita", "Kamat", "abc@gmail.com", "password")
    add_user(new_user)
    add_session(new_user.id)