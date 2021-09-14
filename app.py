from fastapi import FastAPI

from api.pydantic_model import *

app = FastAPI()


@app.get("/")
def home():
    return {"Data": "NadavIsDaBest"}


@app.get("/get/{item_id}")
def get_item(item_id: int):
    return f"Your item id is: {item_id}"


@app.post("/insert_soldier")
def insert_soldier(soldier: SoldierMeta):
    return soldier


@app.post("/insert_department")
def insert_department(dept: DepartmentMeta):
    return dept
