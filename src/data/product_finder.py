# Regras de negocio
from src.models.sqlite.repository.interfaces.products_repository import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder():
    def __init__(
        self, 
        redis_repo: RedisRepositoryInterface, 
        products_repo: ProductsRepositoryInterface
        ) -> None: # Vai se associar com esses dois elementos
        self.__redis_repo = redis_repo
        self.__products_repo = products_repo
    
    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params["product_name"] # Pega o nome do produto
        product = None
        
        product = self.__find_in_cache(product_name) # Tenta achar o produto em cache
        if not product:
            product = self.__find_in_sql(product_name) # Se não achar procura em SQL 
            self.__insert_in_cache(product) # E armazena o dado do sql em cache
            
        return self.__format_reponse(product) # Vai retornar a informação de produto
    
    def __find_in_cache(self, product_name: str) -> tuple:
        product_infos = self.__redis_repo.get_key(product_name) # Vou buscar a informação com a chave no repositorio em cache
        if product_infos:
            product_info_list = product_infos.split(",") # Vai ficar assim: price,quantity -> [price, quantity]
            return (0, product_name, product_info_list[0], product_info_list[1])
        
        return None   

    def __find_in_sql(self, product_name: str) -> tuple:
        product = self.__products_repo.find_product_by_name(product_name)
        if not product: 
            raise Exception("Produto nao encontrado!")
        
        return product
    
    def __insert_in_cache(self, product: tuple) -> None:
        product_name = product[1]
        value = f"{product[2], product[3]}" # 1999.99,10
        self.__redis_repo.insert_expiration(product_name, value, ex=60) # Nome do produto, valor , expiração de 60 segundos em cache
    # Formatação se precisar de levar os dados para um front-end
    def __format_reponse(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "type": "PRODUCT",
                "count": 1,
                "attributes": {
                    "name": product[1], # Casa 1 
                    "price": product[2], # Casa 2
                    "quantity": product[3]
                }
            }
        )  
    