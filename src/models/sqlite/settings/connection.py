import sqlite3
from sqlite3 import Connection as SqliteConnection  # Tipando para ficar mais claro o tipo de conexão que estou usando

class SqliteConnectionHandle:
    def __init__(self) -> None:
        self.__connection_string =  "storage.db"
        self.__conn = None
        
    def connect(self) -> SqliteConnection:
        conn = sqlite3.connect(
            self.__connection_string, 
            check_same_thread=False # Compartilhar uma conexao entrep multiplas threads | sem espera
        )
        self.__conn = conn # Conexão criado no costrutor sendo retornada
        return conn
    
    def get_connection(self) -> SqliteConnection:
        return self.__conn
    