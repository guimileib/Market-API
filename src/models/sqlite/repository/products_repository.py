from sqlite3 import Connection as SqliteConnection
from .interfaces.products_repository import ProductsRepositoryInterface

class ProductsRepository(ProductsRepositoryInterface):
    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn
    
    def find_product_by_name(self, product_name: str) -> tuple:
        cursor = self.__conn.cursor() # Criação do cursor, objeto que irá interagir com banco de dados
        cursor.execute(
            "SELECT * FROM products WHERE name = ?", # Selecionando todos os produtos 
            (product_name,) # A partir de um nome
        )
        product = cursor.fetchone() # Recupera apenas uma linha do resultado da consulta
        return product
    
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
         '''
            INSERT INTO products
                (name, price, quantity)
            VALUES
                (?, ?, ?)
         ''',
         (name, price, quantity,)
        )
        self.__conn.commit() # Fazendo upload e afirmando que as configurações estão corretas
        