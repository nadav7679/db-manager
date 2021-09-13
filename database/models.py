from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Soldier(Base):
    __tablename__ = "soldiers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    favorite_anime = Column(String)
    department_id = Column(String, ForeignKey("Department"))

    commander = relationship("Soldier", remote_side=[name])
    department = relationship("Department", back_populates="slaves")


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    slaves = relationship("Soldier", back_populates="department")
