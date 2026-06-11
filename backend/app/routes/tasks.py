from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.task import Task
from app.schemas import TaskCreate, TaskOut
from app.security import get_current_user


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db), _=Depends(get_current_user)):
    return db.query(Task).all()


@router.post("", response_model=TaskOut)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    task = Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
