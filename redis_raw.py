import redis 

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

redis_conn.set("chave_1", "algum_valor") # Adcionar chave valor no redis e update de valores na chave

meu_valor = redis_conn.get("chave_1").decode("utf-8") # consulta de bytes para string 

redis_conn.delete("chave_1") # delete de dados - no caso uma chave


# Comandos para hash
redis_conn.hset("meu_hash", "nome", "joao") # um field

# Estrutura de como ficaria um hash dentro do DB
meu_hash = { # A chave "meu_hash" 
    "nome": "joao", # chaves, valor do campo
    "idade": 30,
    "cidade": "sao_paulo"
}
# Obserção: o hset funciona tanto para set e insert
redis_conn.hset("meu_hash", "nome", "joao") 
redis_conn.hset("meu_hash", "idade", "30")
redis_conn.hset("meu_hash", "cidade", "sao paulo")

# Consulta em Hash
valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8") # chave, campo
#print(valor_1)

redis_conn.hdel("meu_hash", "cidade") # Deletar um hash - no caso a chave e o campo

# Buscas por existência
elem = redis_conn.exists("chave_1") # Perguntar se uma chave existe
print(elem)

elem2 = redis_conn.hexists("meu_hash", "nome") # Verifica se um hash existe
print(elem2)

# TTL -> Time to Leave - tempo de permanencia do dado no banco, o proprio banco faz a deleção - gerência de memória
# Exemplo TTL:
redis_conn.set("chave_del", "esse valor sera deletado", 15)
redis_conn.expire("meu_hash", 30) # deleção do hash em 30 (conforme tento do db)
