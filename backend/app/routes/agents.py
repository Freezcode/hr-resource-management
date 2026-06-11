from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.action_coordinator import (
    build_action_coordinator_agent,
    orchestrate_analysis,
)
from app.agents.climate_researcher import build_climate_researcher_agent
from app.agents.productivity_analyst import build_productivity_analyst_agent
from app.agents.report_generator import build_report_generator_agent
from app.agents.resource_planner import build_resource_planner_agent
from app.database.db import get_db
from app.security import get_current_user
from app.tools.data_access_tools import get_climate_data, get_productivity_data, get_resource_data


router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/catalog")
def agent_catalog(_=Depends(get_current_user)):
    return {
        "productivity_analyst": build_productivity_analyst_agent(),
        "climate_researcher": build_climate_researcher_agent(),
        "resource_planner": build_resource_planner_agent(),
        "report_generator": build_report_generator_agent(),
        "action_coordinator": build_action_coordinator_agent(),
    }


@router.post("/run")
def run_agent_orchestration(db: Session = Depends(get_db), _=Depends(get_current_user)):
    productivity = get_productivity_data(db)
    climate = get_climate_data(db)
    resources = get_resource_data(db)
    return orchestrate_analysis(productivity, climate, resources)
