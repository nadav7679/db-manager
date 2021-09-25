from fastapi import FastAPI

from api.pydantic_model import *
from database import session
from backend.classes import *
from api.routes import soldier


app = FastAPI()

app.include_router(soldier.router)

@app.get("/")
def home():
    return {"Data": "NadavIsDaBest"}


@app.get("/get/{item_id}")
def get_item(item_id: int):
    return f"Your item id is: {item_id}"


@app.post("/insert_department")
def insert_department(dept: DepartmentMeta):
    session.add(dept.create_department())
    session.commit()
    return dept


@app.post("/get")
def get(filter: GetFilter):
    get_instance = Get(filter)
    # Send filter to backend
    # Return error if caught
    # Return JSON with data if checks out
    print(get_instance.tablename)
    return
