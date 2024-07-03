import sqlite3

class Connection:
    def __init__(self, db_name: str = 'db/database.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: tuple = None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return False