from redis import Redis 

class RedisConnectionHandler:
    def __init__(self) -> None:
        self.__redis_conn = None # Injeção da dependência
    
    # Definindo a conexão com Redis
    def connect(self) -> Redis:
        redis_conn = Redis(
            host="localhost", 
            port=6379, 
            db=0
        )
        self.__redis_conn = redis_conn
        return redis_conn
    
    # Caso precise pegar a conexão com Redis
    def get_connection(self) -> Redis:
        return self.__redis_conn
