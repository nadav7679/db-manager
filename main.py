import os
import time

import dotenv
from sqlalchemy import create_engine
from config import app_config

from database.models import Base


dotenv.load_dotenv("./.env")
env_vars = os.environ
env = env_vars['ENV']

os.system(f"docker run --rm -d -e POSTGRES_USER={env_vars['DB_USERNAME']}"
          f" -e POSTGRES_PASSWORD={env_vars['DB_PASSWORD']} -e POSTGRES_DB={env_vars['DATABASE']}"
          f" -p 5432:5432 --name db_manager postgres")
time.sleep(2)

engine = create_engine(app_config[env].SQLALCHEMY_URI)
print(app_config[env].SQLALCHEMY_URI)
Base.metadata.create_all(bind=engine)