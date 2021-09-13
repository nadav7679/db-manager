from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Soldier(Base):
    __tablename__ = "soldiers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    favorite_anime = Column(String)
    department = Column(String, ForeignKey("departments.name"))

    commander = relationship("Soldier", remote_side=[name])
    _department = relationship("Department", back_populates="slaves")

    def __repr__(self):
        return f'<Soldier: {self.name}, owner: {self.commander}>'


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    king = Column(String, ForeignKey("soldiers.name"), nullable=False)

    _king = relationship("Soldier", back_populates="department")

    def __repr__(self):
        return f'<Department: {self.name}>'
