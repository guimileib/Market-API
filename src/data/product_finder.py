# Regras de negocio
from src.models.sqlite.repository.interfaces.products_repository import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class ProductFinder(ProductsRepositoryInterface):
    def __init__(
        self, 
        redis_repo: RedisRepositoryInterface, 
        products_repo: ProductsRepositoryInterface
        ) -> None: # Vai se associar com esses dois elementos
        self.__redis_repo = redis_repo
        self.__sqlite_repo = products_repo
    
    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        pass
    