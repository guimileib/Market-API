from redis import Redis # tipar parte do projeto
from .interfaces.redis_repository import RedisRepositoryInterface

class RedisRepository(RedisRepositoryInterface):
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn # Injeção de dependência

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value) # lembrando, serve como update e set
        
    def get_key(self, key:str) -> str:
        value = self.__redis_conn.get(key)
        if value: # Verifica se tem valor antes de retornar o decode
            return value.decode("utf-8") 
        return None
    
    def insert_hash(self, key: str, field: str, value:any) -> None:
        self.__redis_conn.hset(key, field, value)
        
    def get_hash(self, key: str, field: str) -> any:
        value = self.__redis_conn.hget(key, field) # get hash para pegar a chave-campo
        if value:
            return value.decode("utf-8")
        return None
    
    def insert_expiration(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.set(key, value, ex=ex) # ex é o tempo de expiração
    
    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, ex)
        