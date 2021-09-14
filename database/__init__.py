import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv

from config import app_config


load_dotenv("../.env")
env_vars = os.environ
env = env_vars['ENV']

engine = create_engine(app_config[env].SQLALCHEMY_URI)
Base = declarative_base()