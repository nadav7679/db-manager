import os

import dotenv

dotenv.load_dotenv()
env = os.environ


class Config:
    SQLALCHEMY_URI = f"postgresql://{env['USERNAME']}:{env['PASSWORD']}@localhost:5432/{env['DATABASE']}"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    'Development': DevelopmentConfig,
    'Production': ProductionConfig
}
