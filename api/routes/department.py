from fastapi import APIRouter

from sqlalchemy import select

from database.models import Department
from database import session
from database.pydantic_model import DepartmentMeta

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.post("/create/")
def create(dept: DepartmentMeta):
    session.add(dept.create_department())
    session.commit()
    return dept


@router.get("/read/")
def read(did: str = None, name: str = None):
    if did is not None:
        select_stmt = select(Department).where(Department.id == did)

    elif name is not None:
        select_stmt = select(Department).where(Department.name == name)

    else:
        select_stmt = select(Department)

    res = session.execute(select_stmt)
    departments = [(dep.id, dep.name) for dep in res.scalars().all()]
    return departments
