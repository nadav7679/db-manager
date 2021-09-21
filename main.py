import os
import time

import dotenv
from sqlalchemy import create_engine
import uvicorn

from config import app_config
from database.models import Base

dotenv.load_dotenv("./.env")
env_vars = os.environ
env = env_vars['ENV']

os.system(f"docker run --rm -d -e POSTGRES_USER={env_vars['DB_USERNAME']}"
          f" -p 5432:5432 --name db_manager postgres")
time.sleep(3)

engine = create_engine(app_config[env].SQLALCHEMY_URI)
Base.metadata.create_all(bind=engine)
import database.upload_data
# if __name__ == "__main__":
#     uvicorn.run("api.app:app", host="0.0.0.0", reload=True, debug=True, workers=1, port=8000)
