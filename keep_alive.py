from flask import Flask
from threading import Thread
import time

total_time_wait = time.time()
app = Flask('')
@app.route('/')
def main():
    return f"Uptime: {round(time.time() - total_time_wait)} seconds"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()