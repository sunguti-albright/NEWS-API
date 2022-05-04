from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    
    Args:
        config_name : name of the configuration to be used
    '''

    # Initialising application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])


    # Initialising flask extensions
    bootstrap.init_app(app)
 # Regestering the main blueprint
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config when using an API
    from .requests import configure_request
    configure_request(app)

    return app