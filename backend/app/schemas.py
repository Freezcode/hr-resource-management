from typing import Optional

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str = Field(min_length=6)
    role: str = "employee"


class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str = "employee"
    department: str


class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    status: str = "open"
    estimated_hours: int = 0
    actual_hours: int = 0
    is_blocked: bool = False
    assignee_id: Optional[int] = None


class TaskOut(TaskCreate):
    id: int

    class Config:
        from_attributes = True


class SurveyCreate(BaseModel):
    employee_id: int
    engagement_score: int = Field(ge=1, le=10)
    stress_score: int = Field(ge=1, le=10)
    sentiment: str
    comment: Optional[str] = None


class SurveyOut(SurveyCreate):
    id: int

    class Config:
        from_attributes = True
