from typing import Any

from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.survey import SurveyResponse
from app.models.task import Task


def get_productivity_data(db: Session) -> dict[str, Any]:
    tasks = db.query(Task).all()
    total = len(tasks)
    completed = len([t for t in tasks if t.status.lower() == "done"])
    blocked = len([t for t in tasks if t.is_blocked])
    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "completion_rate": (completed / total * 100) if total else 0,
        "blocked_tasks": blocked,
    }


def get_climate_data(db: Session) -> dict[str, Any]:
    responses = db.query(SurveyResponse).all()
    count = len(responses)
    if not count:
        return {"responses": 0, "engagement_avg": 0, "stress_avg": 0}

    engagement_avg = sum(r.engagement_score for r in responses) / count
    stress_avg = sum(r.stress_score for r in responses) / count
    return {"responses": count, "engagement_avg": round(engagement_avg, 2), "stress_avg": round(stress_avg, 2)}


def get_resource_data(db: Session) -> dict[str, Any]:
    employees = db.query(Employee).all()
    tasks = db.query(Task).all()
    workload: dict[int, int] = {}
    for task in tasks:
        if task.assignee_id is not None:
            workload[task.assignee_id] = workload.get(task.assignee_id, 0) + 1

    overloaded = [employee_id for employee_id, count in workload.items() if count > 5]
    return {
        "employees": len(employees),
        "tasks": len(tasks),
        "overloaded_employees": overloaded,
        "avg_tasks_per_employee": (len(tasks) / len(employees)) if employees else 0,
    }
