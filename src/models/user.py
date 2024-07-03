
from src.database.connection import * 

class User:
    def __init__(self):
        self.connection = Connection()

    def create_table_user(self, table_name: str, columns: str):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        return self.connection.execute_query(query)

    def insert_data(self, table_name: str, columns: str, values: tuple):
        placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        return self.connection.execute_query(query, (values))
    
    def get_user_authentication(self, table_name: str, login: str, password: str):
        query = f"SELECT * FROM {table_name} WHERE login = ? AND password = ? "
        self.connection.execute_query(query, (login, password))
        result = self.connection.cursor.fetchone()

        if result:
            return result # Retorna o valor da coluna desejada do último registro
        else:
            return None

