from fastapi import APIRouter
from sqlalchemy import select

from database import session
from api.pydantic_model import *
from backend.classes import *

router = APIRouter(prefix="/soldiers", tags=["Soldiers"])


@router.post("/insert_soldier")
def insert_soldier(soldier: SoldierMeta):
    session.add(soldier.create_soldier())
    session.commit()
    return soldier


@router.get("/get/")
def get(name: str = None, sid: int = None):
    if sid is not None:
        select_stmt = select(Soldier).where(Soldier.id == sid)

    elif name is not None:
        select_stmt = select(Soldier).where(Soldier.name == name)

    else:
        select_stmt = select(Soldier)

    res = session.execute(select_stmt)
    soldiers = [(soldier.name, soldier.id) for soldier in res.scalars().all()]
    return soldiers






