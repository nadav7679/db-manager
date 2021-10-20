from typing import Optional, Literal
from pydantic import BaseModel, conlist
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database.models import *

tablenames = classnames.keys()

TempSoldierMeta = sqlalchemy_to_pydantic(Soldier)
TempDepartmentMeta = sqlalchemy_to_pydantic(Department)

class SoldierMeta(TempSoldierMeta):
    def create_soldier(self):
        slave = Soldier(name=self.soldier_name,
                        department=self.soldier_department,
                        commander=self.soldier_commander,
                        favorite_anime=self.anime
                        )

        return slave


class DepartmentMeta(TempDepartmentMeta):
    def create_department(self):
        dept = Department(
            name=self.name,
            king=self.king
        )

        return dept


class BaseFilter(BaseModel):
    tablename: Literal[tuple(tablenames)]


class GetFilter(BaseFilter):
    columns: Optional[conlist(str, min_items=1)] = None
    where: str
    order_by: Optional[conlist(str, min_items=1)] = None
