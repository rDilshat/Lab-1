import psycopg2
import csv

class PhoneBookRepository:
    def __init__(self, db_config):
        
        #Connect to Data Base
        self.connection = psycopg2.connect(
            dbname=db_config.get('dbname'),
            user=db_config.get('user'),
            password=db_config.get('password'),
            host=db_config.get('host', 'localhost'),
            port=db_config.get('port', 5432)
        )
        self.cursor = self.connection.cursor()

    def upload_from_csv(self, csv_file_path):

        #Function, which opens csv file
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row if present
            for row in reader:
                user_name, phone = row
                self.insert_entry(user_name, phone)

    def insert_entry(self, user_name, phone):
        
        #Uploading values to table
        query = "INSERT INTO phone_book (user_name, phone) VALUES (%s, %s)"
        self.cursor.execute(query, (user_name, phone))
        self.connection.commit()

    def update_entry(self, user_name=None, phone=None, new_user_name=None, new_phone=None):
      
        if user_name and new_user_name:
            query = "UPDATE phone_book SET user_name = %s WHERE user_name = %s"
            self.cursor.execute(query, (new_user_name, user_name))
        if phone and new_phone:
            query = "UPDATE phone_book SET phone = %s WHERE phone = %s"
            self.cursor.execute(query, (new_phone, phone))
        self.connection.commit()

    def query_entries(self, user_name=None, phone=None):
        
        if user_name:
            query = "SELECT * FROM phone_book WHERE user_name = %s"
            self.cursor.execute(query, (user_name,))
        elif phone:
            query = "SELECT * FROM phone_book WHERE phone = %s"
            self.cursor.execute(query, (phone,))
        else:
            query = "SELECT * FROM phone_book"
            self.cursor.execute(query)
        
        return self.cursor.fetchall()

    def delete_entry(self, user_name=None, phone=None):
        
        if user_name:
            query = "DELETE FROM phone_book WHERE user_name = %s"
            self.cursor.execute(query, (user_name,))
        elif phone:
            query = "DELETE FROM phone_book WHERE phone = %s"
            self.cursor.execute(query, (phone,))
        
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.cursor.close()
        self.connection.close()

repository = PhoneBookRepository({
    "dbname" : "phonebook",
    "user" : "postgres",
    "password" : "postgres"
})

# repository.insert_entry(input("Enter name: "), input("Enter phone: "))
# repository.update_entry(input("Enter old name: "), input("Enter old phone: "), input("Enter "), input())
# repository.upload_from_csv("csv_file_path.csv")
# print(repository.query_entries())
# print(repository.query_entries(input()))
# print(repository.query_entries(None, input()))