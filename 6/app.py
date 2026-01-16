import redis
r = redis.Redis(host="redis", port=6379)
r.incr("Count")
print("Count ", r.get("Count").decode())