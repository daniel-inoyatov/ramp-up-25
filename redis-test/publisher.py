# publisher.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()
# “redis” here is the Docker‐Compose hostname we’ll define later
r = redis.Redis(host="redis", port=6379, db=0)

class Message(BaseModel):
    text: str

@app.post("/publish")
async def publish(msg: Message):
    channel = "my_channel"
    count = r.publish(channel, msg.text)
    if count == 0:
        # no subscribers listening right now
        raise HTTPException(404, "No subscribers on channel")
    return {"published": msg.text, "subscribers": count}
