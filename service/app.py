from flask import Flask

import service.config as config
from service.api import api
from service.logger import setup_logger


def create_app():
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__)
    app.config.from_object(config.Config)

    # Set up logging
    setup_logger(config.Config.LOG_FILE)

    # Register the API blueprint
    app.register_blueprint(api, url_prefix="/api")

    return app
