import os
from app import app
from app.routes import *
from config import ServiceConfig

# config para o Oracle usar UTF-8
os.environ["NLS_LANG"] = ".AL32UTF8"

port = os.getenv('PORT') or 8102

ServiceConfig.configure('servidor-api', port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
