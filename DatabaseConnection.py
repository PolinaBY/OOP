import psycopg2
from psycopg2.extras import DictCursor

class DBConnection:
    """Класс для работы с базой данных (Одиночка)."""
    
    _instance = None
    
    def __new__(cls, host, user, password, database, port=3306):
        """Гарантирует, что будет создан только один экземпляр соединения с базой данных."""
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance._connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=database,
                port=port,
                cursor_factory=DictCursor
            )
        return cls._instance
    
    def get_connection(self):
        """Возвращает соединение с базой данных."""
        return self._connection
    
    def close_connection(self):
        """Закрывает соединение с БД."""
        if self._connection:
            self._connection.close()
            DBConnection._instance = None
