import os

import dotenv

dotenv.load_dotenv("./.env")
env = os.environ
os.system(f"docker run --rm -d -e POSTGRES_PASSWORD={env['PASSWORD']} -e POSTGRES_DB={env['DATABASE']}"
          f" -p 5432:5432 --name db_manager postgres")