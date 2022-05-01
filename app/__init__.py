from flask import Flask
from .config import DevConfig

if __name__ == '__main__':
    app = Flask(__name__)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views