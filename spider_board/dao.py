import redis

host="127.0.0.1"
port=6379

redis_conn_15=redis.Redis(host, port, db=15)
redis_conn_1=redis.Redis(host,port,db=1)