from flask import Flask
import redis
import time

## Redis database
cache = redis.Redis(host='redis', port=6379,decode_responses=True)

## Flask
app = Flask(__name__)

@app.route("/api")
def visitor():
    while True:
        try:
            counter = cache.incr('visits', amount=1)
        except redis.exceptions.ConnectionError:
            time.sleep(3)
            continue
        return f"<p>Hello, you are visitor number: {counter}</p>"