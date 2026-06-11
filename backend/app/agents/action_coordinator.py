from typing import Any

from app.agents.climate_researcher import analyze_climate, build_climate_researcher_agent
from app.agents.productivity_analyst import analyze_productivity, build_productivity_analyst_agent
from app.agents.report_generator import build_report_generator_agent, generate_report
from app.agents.resource_planner import analyze_resources, build_resource_planner_agent

try:
    from crewai import Crew, Task
except Exception:
    Crew = None
    Task = None


def build_action_coordinator_agent() -> dict[str, str]:
    return {
        "role": "Action Coordinator",
        "goal": "Orchestrate all insights into implementation plans and tracked actions",
    }


def orchestrate_analysis(productivity_data: dict, climate_data: dict, resource_data: dict) -> dict:
    productivity_insights = analyze_productivity(productivity_data)
    climate_insights = analyze_climate(climate_data)
    resource_insights = analyze_resources(resource_data)

    report = generate_report(productivity_insights, climate_insights, resource_insights)
    action_plan = {
        "priority_actions": [
            *productivity_insights.get("insights", []),
            *climate_insights.get("recommendations", []),
            *resource_insights.get("actions", []),
        ]
    }

    if Crew is not None and Task is not None:
        report["crew_configured"] = True
    else:
        report["crew_configured"] = False

    return {"report": report, "action_plan": action_plan}
