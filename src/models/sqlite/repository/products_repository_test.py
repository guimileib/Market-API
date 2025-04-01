import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

# Testes de Integração
@pytest.mark.skip(reason='Interação Banco de dados')
def test_insert_products():
    repo = ProductsRepository(conn)
    
    name = "algumaCoisa2"
    price = 14.34
    quantity = 9
    
    repo.insert_product(name, price, quantity) 

def test_find_product():
    repo = ProductsRepository(conn)
    
    name = "algumaCoisa2"
    response = repo.find_product_by_name(name)
    print(response)
    
