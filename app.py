import time
from datetime import datetime

import redis
import psycopg2
from flask import Flask, request

app = Flask(__name__)
cache = redis.Redis(host='redishost', port=6379)

# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="counter_db",
        user="user",
        password="password"
    )
    return conn

# Функция для увеличения счетчика
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    client_info = request.user_agent.string
    timestamp = datetime.now()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO table_Counter (datetime, client_info) VALUES (%s, %s);",
        (timestamp, client_info)
    )
    conn.commit()
    cur.close()
    conn.close()

    return f'Hello World! I have been seen {count} times.\n'
