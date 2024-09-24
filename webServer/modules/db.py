import mysql.connector
import os

db_password = os.environ['MYSQL_ROOT_PASSWORD']

class db_handler:
    def __init__(self) -> None:
        
        self.config = {
            "host":'database',
            "user":'root',
            "password": db_password,
            "database":'continuum'
        }

    def qury(self, qury):

        try:
            database = mysql.connector.connect(**self.config)
        
        except mysql.connector.errors.DatabaseError as err:
        
            return "Database error"

        cursor = database.cursor(dictionary=True)
        cursor.execute(qury)
        response = cursor.fetchall()
        cursor.close()
        database.close()

        return response

    def insert(self, qury):

        try:
            database = mysql.connector.connect(**self.config)
        
        except mysql.connector.errors.DatabaseError as err:
        
            return "Database error"

        cursor = database.cursor(dictionary=True)
        cursor.execute(qury)
        database.commit()
        response = cursor.fetchall()
        cursor.close()
        database.close()

        return response

if __name__ == '__main__':
    print('This script is not ment to be run alone')