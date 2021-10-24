from fastapi import APIRouter
from sqlalchemy import select

from database import session
from database.pydantic_model import *

router = APIRouter(prefix="/soldiers", tags=["Soldiers"])


@router.post("/create/")
def create(soldier: SoldierMeta):
    session.add(soldier.create())
    session.commit()
    return soldier


@router.get("/read/")
def read(sid: int = None, name: str = None):
    if sid is not None:
        select_stmt = select(Soldier).where(Soldier.id == sid)

    elif name is not None:
        select_stmt = select(Soldier).where(Soldier.name == name)

    else:
        select_stmt = select(Soldier)

    res = session.execute(select_stmt)
    soldiers = [(soldier.id, soldier.name) for soldier in res.scalars().all()]
    return soldiers






