import os


class Config:
    """Base Flask configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key")
    MODEL_PATH = "model/model-best"  # Path to the saved spaCy model
    LOG_FILE = "logs/app.log"

class DevelopmentConfig(Config):
    """Development environment."""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment."""
    DEBUG = False
