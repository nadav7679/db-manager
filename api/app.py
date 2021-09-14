from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Data": "NadavIsDaBest"}


@app.get("/get/{item_id}")
def get_item(item_id: int):
    return f"Your item id is: {item_id}"
