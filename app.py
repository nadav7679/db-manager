from fastapi import FastAPI
import uvicorn

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
    filter = filter.dict()
    print(filter)
    get_instance = Get(filter)
    res = get_instance.get_data()
    # Return error if caught
    # Return JSON with data if checks out
    # print(res.scalars())
    # print([row.__dict__ for row in res.fetchall()])
    if filter['columns'] is None:
        return [row.__dict__ for row in res.scalars()]

    else:
        return [dict(row) for row in res]

@app.post("/post")
def post(filter: PostFilter):
    filter = filter.dict()
    print(filter)
    post_instance = Post(filter)
    res = post_instance.post_data()
    return res


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)