import redis
import os
def environment_variable():
    Host = "localhost"
    Port = 6379
    if 'host' in os.environ:
        Host = os.environ['host']
    if 'port' in os.environ:
        Port = os.environ['port']
    return Host,Port
def connect_redis(Host,Port):
    redis_db = redis.StrictRedis(host=Host, port=Port, db=0)
    if redis_db:
        print("Connected Succefully ",redis_db)
    else:
        print("Problem To Connect Redis")
        os.exit()
    return redis_db

def push(redis_cli,key,value):
    x = redis_cli.lpush(key,value)
    print("after pushing")
    m = redis_cli.lrange(key,0,3)
    print(m)

def pop(redis_cli,key):
    x = redis_cli.lpop(key)
    print("after poping")
    m = redis_cli.lrange(key,0,3)
    print(m)

if __name__ == "__main__":
    host,port = environment_variable()
    redis_cli = connect_redis(host,port)
    push(redis_cli,"name","vaibhav")
