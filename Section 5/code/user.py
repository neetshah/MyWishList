import sqlite3

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def find_by_username(self, username):
        connection = sqlite3.connect('data.db')
        cursor = connetion.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username, ))
        row = result.fetchone()
        if row: 
            user = User(row[0], row[1], row[2])
        else:
            user= None

        connection.close()
        return user