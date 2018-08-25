import sqlite3
from flask_restful import Resource

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connetion.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username, ))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user= None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connetion.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id, ))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user= None

        connection.close()
        return user

class UserRegister(Resource):
    def post(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"

        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
