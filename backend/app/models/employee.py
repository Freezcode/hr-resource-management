from sqlalchemy import Column, Integer, String

from app.database.db import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(160), unique=True, index=True, nullable=False)
    role = Column(String(50), nullable=False, default="employee")
    department = Column(String(80), nullable=False)
