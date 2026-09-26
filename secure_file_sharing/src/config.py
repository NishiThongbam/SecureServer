import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAX_CONNECTIONS=5

HOST='127.0.0.1'
PORT=8080

LOG_DIR = os.path.join(BASE_DIR, 'data', 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'server.log')

