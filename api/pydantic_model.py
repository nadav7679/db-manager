from typing import Optional
from pydantic import BaseModel

from database.models import *


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
