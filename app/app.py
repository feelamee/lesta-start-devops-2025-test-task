from flask import Flask, jsonify
from redis import Redis

import os

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify(status='ok')

@app.route('/count')
def count():
    redis.incr('count')
    count = str(redis.get('count'), 'utf-8')
    return 'The meaning of life' if count == '42' else count

APP_PORT = os.getenv('APP_PORT', 5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT)
