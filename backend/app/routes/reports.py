from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.action_coordinator import orchestrate_analysis
from app.database.db import get_db
from app.security import get_current_user
from app.tools.data_access_tools import get_climate_data, get_productivity_data, get_resource_data


router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/dashboard")
def dashboard_report(db: Session = Depends(get_db), _=Depends(get_current_user)):
    productivity = get_productivity_data(db)
    climate = get_climate_data(db)
    resources = get_resource_data(db)
    return orchestrate_analysis(productivity, climate, resources)
