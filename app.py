from fastapi import FastAPI

from database.pydantic_model import *
from database import session
from backend.classes import *
from api.routes import soldier, department


app = FastAPI()

app.include_router(soldier.router)
app.include_router(department.router)

@app.get("/")
def home():
    return {"Data": "NadavIsDaBest"}

@app.post("/get")
def get(filter: GetFilter):
    get_instance = Get(filter)
    # Send filter to backend
    # Return error if caught
    # Return JSON with data if checks out
    print(get_instance.tablename)
    return
