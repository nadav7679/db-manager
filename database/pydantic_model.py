from typing import Optional, Literal, Tuple, Dict, TypedDict, List, NamedTuple
from pydantic import BaseModel, conlist

from database.models import *

tablenames = classnames.keys()
schemanames = ["public", "test"]


class SoldierMeta(BaseModel):
    soldier_name: str
    soldier_department: str
    soldier_commander: str
    anime: Optional[str] = None

    def create_soldier(self):
        slave = Soldier(name=self.soldier_name,
                        department=self.soldier_department,
                        commander=self.soldier_commander,
                        favorite_anime=self.anime
                        )

        return slave


class DepartmentMeta(BaseModel):
    name: str
    king: str

    def create_department(self):
        dept = Department(
            name=self.name,
            king=self.king
        )

        return dept


class BaseFilter(BaseModel):
    table: Literal[tuple(tablenames)]
    schemaName: Literal[tuple(schemanames)]


class OrderBy(TypedDict):
    columns: conlist(str, min_items=1)
    order: conlist(Literal[("desc", "asc")], min_items=1)
# Make sure order length is exactly the order of columns!


class GetFilter(BaseFilter):
    columns: Optional[conlist(str, min_items=1)] = None
    where: Optional[str] = None
    orderBy: Optional[OrderBy] = None
    limit: Optional[int] = None
