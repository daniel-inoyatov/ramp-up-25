# subscriber.py
import redis

def main():
    r = redis.Redis(host="redis", port=6379, db=0)
    p = r.pubsub()
    p.subscribe("my_channel")
    print("Waiting for messages…", flush=True)
    for msg in p.listen():
        if msg["type"] == "message":
            print("Received:", msg["data"].decode(),flush=True)

if __name__ == "__main__":
    main()
