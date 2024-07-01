from flask import Flask
import os

app = Flask(__name__)

@app.route('/home')
def home():
    return f'Server ID: {os.getenv("SERVER_ID", "unknown")}'

@app.route('/heartbeat')
def heartbeat():
    return '', 204  # HTTP 204 No Content for health check

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
