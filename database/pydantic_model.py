from typing import Optional, Literal, Tuple, Dict, TypedDict, List, NamedTuple
from pydantic import BaseModel, conlist

from database.models import *

tablenames = classnames.keys()
schemanames = ["public", "test"]
databases = ["postgres", "test", "db-manager"]

class SoldierMeta(BaseModel):
    name: str
    department: str
    commander: str
    favorite_anime: Optional[str] = None

    def create(self):
        slave = Soldier(name=self.name,
                        department=self.department,
                        commander=self.commander,
                        favorite_anime=self.favorite_anime
                        )

        return slave


class DepartmentMeta(BaseModel):
    name: str
    king: str

    def create(self):
        dept = Department(
            name=self.name,
            king=self.king
        )

        return dept


class BaseFilter(BaseModel):
    database: Literal[tuple(databases)]
    schemaName: Literal[tuple(schemanames)]
    table: Literal[tuple(tablenames)]


class OrderBy(TypedDict):
    columns: conlist(str, min_items=1)
    order: conlist(Literal[("desc", "asc")], min_items=1)
# Make sure order length is exactly the order of columns!



class GetFilter(BaseFilter):
    columns: Optional[conlist(str, min_items=1)] = None
    where: Optional[str] = None
    orderBy: Optional[OrderBy] = None
    limit: Optional[int] = None


class PostFilter(BaseFilter):
    rowsCount: Optional[int] = 1
    data: dict

meta = {"soldiers": SoldierMeta, "departments": DepartmentMeta}