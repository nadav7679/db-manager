from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Soldier(Base):
    __tablename__ = "soldiers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    department = Column(String, ForeignKey("departments.name"))
    commander = Column(String, ForeignKey("soldiers.name"))
    favorite_anime = Column(String)

    _commander = relationship("Soldier", remote_side=[name], foreign_keys=[commander])
    _department = relationship("Department", foreign_keys=[department])

    def __repr__(self):
        return f'<Soldier: {self.name}, owner: {self.commander}>'


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    king = Column(String, ForeignKey("soldiers.name"))

    _king = relationship("Soldier", foreign_keys=[king])

    def __repr__(self):
        return f'<Department: {self.name}, king: {self.king}>'


classnames = {"soldiers": Soldier, "departments": Department}